Postmortem: Lyrics Breaker Outage
Issue Summary
Duration: August 10, 2024, 14:00 - 16:30 EAT
Impact: The Lyrics Breaker website experienced a complete outage, affecting 100% of users. Users were unable to access the site, resulting in a significant disruption of service.
Root Cause: The root cause was a misconfiguration in the Nginx server, which led to a failure in handling incoming HTTP requests.
Timeline
14:00: Issue detected via monitoring alert indicating a spike in 500 Internal Server Error responses.
14:05: Initial investigation began by checking the application logs and server status.
14:15: Assumed the issue was related to a recent code deployment; rolled back the deployment, but the issue persisted.
14:30: Noticed that the Nginx server was not properly forwarding requests to the backend.
14:45: Misleading path: Spent time checking database connections and backend service health, which were all functioning correctly.
15:00: Escalated to the DevOps team for further investigation.
15:15: DevOps team identified a misconfiguration in the Nginx configuration file.
15:30: Corrected the Nginx configuration and restarted the server.
15:45: Verified that the site was back online and functioning correctly.
16:00: Monitoring confirmed that the issue was resolved.
16:30: Postmortem analysis and documentation began.
Root Cause and Resolution
Root Cause: The Nginx configuration file had an incorrect directive that caused the server to fail in forwarding requests to the backend application. Specifically, the proxy_pass directive was pointing to an incorrect backend address, leading to 500 Internal Server Errors.
Resolution: The issue was resolved by correcting the proxy_pass directive in the Nginx configuration file. The correct backend address was specified, and the Nginx server was restarted to apply the changes. This restored the proper handling of incoming HTTP requests, and the site became accessible again.
Corrective and Preventative Measures
Improvements:
Configuration Management: Implement a more robust configuration management process to ensure that configuration changes are reviewed and tested before deployment.
Monitoring and Alerts: Enhance monitoring to include specific checks for Nginx configuration and request forwarding.
Documentation: Update the documentation to include detailed steps for verifying Nginx configuration and common troubleshooting steps.
Tasks:
Patch Nginx Server: Ensure that the Nginx server is updated to the latest stable version.
Add Monitoring: Implement monitoring for Nginx configuration changes and request forwarding status.
Automate Configuration Checks: Develop scripts to automatically check and validate Nginx configuration before deployment.
Training: Conduct training sessions for the team on best practices for Nginx configuration and troubleshooting.
Review Deployment Process: Review and improve the deployment process to include configuration validation steps.
By addressing these areas, we aim to prevent similar issues in the future and ensure a more resilient and reliable service for our users.

