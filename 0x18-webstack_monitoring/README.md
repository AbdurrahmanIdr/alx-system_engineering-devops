# Webstack Monitoring
Webstack Monitoring is a project aimed at implementing tools to measure and monitor the performance and behavior of our software systems. It involves two categories of monitoring: application monitoring and server monitoring. This project provides instructions on how to set up monitoring using Datadog, a popular monitoring and analytics platform.

## Getting Started
To set up webstack monitoring using Datadog, follow the steps outlined in the project requirements. These steps include signing up for a Datadog account, installing the Datadog agent on the web server (web-01), and creating an application key for monitoring specific applications.

## Prerequisites
Ubuntu 16.04 LTS server
Access to the web-01 server
Internet connection to sign up for Datadog and download the Datadog agent
## nstallation
### Sign up for a free Datadog account at https://www.datadoghq.com/.

### Follow the instructions provided on the website to install the Datadog agent on the web-01 server. Use the following command:

```DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=<DATADOG_API_KEY> DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"
Replace <DATADOG_API_KEY> with your Datadog API key.
