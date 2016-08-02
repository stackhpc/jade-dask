# jupyterhub_config.py
c = get_config()

import os
pjoin = os.path.join

runtime_dir = os.path.join('/srv/jupyterhub')

c.JupyterHub.port = 8000

c.JupyterHub.db_url = pjoin(runtime_dir, 'jupyterhub.sqlite')

# use GitHub OAuthenticator for local users
c.JupyterHub.authenticator_class = 'oauthenticator.LocalGitHubOAuthenticator'
c.GitHubOAuthenticator.oauth_callback_url = 'https://dev.jupyter.informaticslab.co.uk/hub/oauth_callback'

# create system users that don't exist yet
c.LocalAuthenticator.create_system_users = True

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# Spawn user containers from this image
c.DockerSpawner.container_image = 'jupyter/scipy-notebook'
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.links = {'master_jupyter_1': 'jupyterhub'}
c.DockerSpawner.hub_ip_connect = 'jupyterhub'

# Have the Spawner override the Docker run command
c.DockerSpawner.extra_create_kwargs.update({
    'command': '/usr/local/bin/start-singleuser.sh'
})


# specify users and admin
c.Authenticator.whitelist = {'niallrobinson'}
c.Authenticator.admin_users = {'niallrobinson'}