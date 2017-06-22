The API notebooks are all executable! Hit "enter" in any code cell to execute it (and all cells before it that have not executed yet), or scroll to the bottom of the notebook and click "Play notebook". For more information, see [http://apinotebook.com](http://apinotebook.com).

#Considerations

- In order to run these notebooks you will need a GitHub account. At some point of the execution, you will be prompted to authorize the client application to access to your account.
- You should register a GitHub application at [https://github.com/settings/applications/new](https://github.com/settings/applications/new). Authorization callback URL of your application must be set to [https://api-notebook.anypoint.mulesoft.com/authenticate/oauth.html](https://api-notebook.anypoint.mulesoft.com/authenticate/oauth.html). At some point of the run, you will be prompted to enter the clientId and clientSecret of your own application.
- In order to run "Users, orgs and teams" and "Repos part 2" notebooks you should register an organization at [https://github.com/account/organizations/new](https://github.com/account/organizations/new). In the very beginning of each notebook you will be prompted to enter the organization ID.
- The "Users, orgs and teams" notebook asks you to provide some GitHub user ID. During notebook execution this User will be added to your organization and team and removed from them later on. Do not enter your own ID as you can not be removed from your own organization. Remember, that you must have access to the users email.
