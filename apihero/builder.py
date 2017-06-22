import os
import yaml
import pyraml.parser
import shutil
from mako.lookup import TemplateLookup
from mako.exceptions import RichTraceback


class Builder:
    src = None
    config = None
    base_dir = ''
    base_url = ''
    src_dir = ''
    output_dir = ''
    template_dir = ''
    template_name = ''

    def __init__(self, base_dir, output_dir, base_url='', template_name='default'):
        os.makedirs(output_dir, exist_ok=True)
        self.base_dir, self.output_dir, self.base_url = base_dir, output_dir, base_url
        self.config = yaml.load(open(os.path.join(self.base_dir, 'config.yaml'), 'r'))
        self.src_dir = os.path.join(self.base_dir, 'src')
        if not os.path.exists(self.src_dir):
            raise LookupError('Cannot found source directory (%s).' % self.src_dir)
        self.src = pyraml.parser.load(os.path.join(self.src_dir, 'api.raml'))

        self.template_name = template_name
        self.template_dir = os.path.join(os.path.dirname(__file__), 'templates', template_name)
        self.template_lookup = TemplateLookup(directories=[self.template_dir])

        if not os.path.exists(self.template_dir):
            self.template_dir = os.path.join(self.base_dir, 'templates', template_name)
            if not os.path.exists(self.template_dir):
                raise LookupError('Cannot found template directory (%s).' % self.template_dir)

    def render(self, filename, data):
        # noinspection PyTypeChecker
        base_data = dict(
            base_url=self.base_url,
            resource_filename=self.get_resource_filename,
        )
        base_data.update(data)
        # noinspection PyBroadException
        try:
            return self.template_lookup.get_template(filename).render(**base_data)
        except:
            traceback = RichTraceback()
            for (filename, line_no, func_name, line) in traceback.traceback:
                print("File %s, line %s, in %s" % (filename, line_no, func_name))
                print(line, "\n")
            print("%s: %s" % (str(traceback.error.__class__.__name__), traceback.error))

    @staticmethod
    def get_resource_filename(resource_path):
        resource_path = 'index' if resource_path == '' else str(resource_path).replace('/', '+')
        return resource_path + '.html'

    def write(self, resource_path, content):
        path = os.path.join(self.output_dir, self.get_resource_filename(resource_path))

        # print(path, resource_path)
        with open(path, 'w+') as f:
            f.write(content)

    @classmethod
    def collect(cls, resource, base='', base_list=None):
        base_list = [] if base_list is None else base_list
        resource._collect_path = base
        resource._collect_path_list = base_list
        resources = [resource]
        if resource.resources is not None:
            for e in resource.resources:

                x = list()
                x.extend(base_list)
                x.append(e)
                resources.extend(cls.collect(resource.resources[e], ''.join([base, e]), x))
        return resources

    def copy_template_statics(self):
        template_assets_path = os.path.join(self.template_dir, "static")
        if os.path.isdir(template_assets_path):
            shutil.copytree(template_assets_path, os.path.join(self.output_dir, "static"))

    def clear_output(self):
        if os.path.isdir(self.output_dir):
            shutil.rmtree(self.output_dir)


class SinglePageBuilder(Builder):
    pass


class MultiPageBuilder(Builder):

    # noinspection PyTypeChecker
    # noinspection PyProtectedMember
    def build(self):
        template_data = dict()
        template_data['resources_path'] = ''
        template_data['title'] = self.src.title
        template_data['author'] = self.config['author']
        template_data['meta_title'] = self.src.title
        template_data['version'] = self.src.version
        template_data['short_description'] = self.src.title
        template_data['root_resource'] = self.src
        template_data['all_resources'] = self.collect(self.src)

        # Prepare output
        self.clear_output()
        self.copy_template_statics()

        # Write output
        for resource in template_data['all_resources']:
            template_data['resource'] = resource
            output = self.render('resource.mako', template_data)
            self.write(resource._collect_path, output)
