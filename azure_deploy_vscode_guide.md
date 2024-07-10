# Azure Deployment of Django Web Apps

## A deployment guide for Azure with SQLite in VS Code

1. Go to [Azure.com](azure.com) to register an account.  Select Pay-As-Go to get the first year free.

2. In VS Code make sure you install the Azure extensions in the Extensions attribute. Click on the Azure icon and add a App Service with the plus sign in the Azure area.  It will ask you to login and confirm your Subscription. Use the free tier for your experimentation. Follow the instruction to create the App Service.

3. Once the App Service is created, click on the File Explorer icon.  Right click on the djangobaseproject folder in your VS Code and select "Deploy to Web App".  Follow the instructions to deploy to the App Service you just created. Deployment may take a few minutes.

4. Once deployment is confirmed, navigate to Azure to confirm deployment to the website.  If any problems arise, click on App Services >> App Monitoring >> Logs to see what problems arose from deployment and the server.

Here is a an example on Azure of the base website: [https://djangobaseproject.azurewebsites.net/](https://djangobaseproject.azurewebsites.net/).  
