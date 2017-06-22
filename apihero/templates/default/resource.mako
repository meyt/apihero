<%inherit file="master.mako"/>

<div class="resource-description">

    % if hasattr(resource, 'displayName') and resource.displayName:
        <h1>${resource.displayName}</h1>
    % endif


    % if hasattr(resource, 'description') and resource.description:
        <p>${resource.description}</p>
    % endif


    % if hasattr(resource, 'documentation') and resource.documentation:
        % for document in resource.documentation:
            <h2>${document.title}</h2>
            <p>${document.content}</p>
        % endfor
    % endif


    % if hasattr(resource, 'methods') and resource.methods:
    <h2>Methods: </h2>
    <ul class="nav nav-tabs">
        % for method in resource.methods:
        <li><a data-toggle="tab" href="#method-content-${method}">${method}</a></li>
        % endfor
    </ul>

    <div class="tab-content">
        % for method in resource.methods:
        <div id="method-content-${method}" class="tab-pane fade">
            <h3>${str(method).title}</h3>
            % if resource.methods[method].description:
            <p>${resource.methods[method].description}</p>
            % endif


            % if resource.methods[method].queryParameters:
                <h4>Parameters:</h4>
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>Parameter</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
                    % for query_parameter in resource.methods[method].queryParameters:
                        <%
                        description = resource.methods[method].queryParameters[query_parameter].description
                        if not description:
                            description = ''
                        required = resource.methods[method].queryParameters[query_parameter].required
                        if required:
                            required = '<span class="label label-danger">Required</span>'
                        else:
                            required = ''

                        type_ = resource.methods[method].queryParameters[query_parameter].type
                        if '':
                            type = 'Type: <span class="label label-default">%s</span>' % type_
                        else:
                            type_ = ''
                        %>
                        <tr>
                            <td>
                                % if displayName:
                                    <p>${displayName}</p>
                                    <p><small><i>${query_parameter}</i></small></p>
                                % else:
                                    <p>${query_parameter}</p>
                                % endif
                                ${required}
                            </td>
                            <td>
                                <p>${description}</p>
                                <p>${type_}</p>
                            </td>
                        </tr>
                    % endfor
                    </tbody>
                </table>
            % endif
        </div>
        % endfor
    </div>
    % endif


    % if resource.resources:
    <h2>Resources: </h2>
    <ul class="list-group">
        % for resource_in in resource.resources:
        <li class="list-group-item">
            <a href="${resource_filename(resource._collect_path + resource_in)}">
                ${resource_in}
            </a>
            % if resource.resources[resource_in].methods:
            % for method_name in resource.resources[resource_in].methods:
            <span class="badge bg-primary">
                ${method_name}
            </span>
            % endfor
            % endif
        </li>
        % endfor
    </ul>
    % endif
</div>