# Image-Background-Remover
Sure, here's a step-by-step tutorial for deploying a Flask application that removes the background from an image to an EC2 instance on AWS:

## Prerequisites

Before you begin, make sure you have the following:

- An AWS account
- An EC2 instance running a Linux-based operating system (e.g. Amazon Linux, Ubuntu, etc.)
- SSH access to the EC2 instance
- Python and pip installed on the EC2 instance
- A working Flask application that removes the background from an image

## Steps

1. Copy the Flask application files to the EC2 instance

   - In your local machine, navigate to the root directory of your Flask application
   - Use the `scp` command to copy the files to the EC2 instance:
   ````
   scp -i /path/to/key.pem * ec2-user@<ec2-instance-public-ip>:/path/to/destination
   ```
   - Replace `/path/to/key.pem` with the path to your SSH key file, `<ec2-instance-public-ip>` with the public IP address of your EC2 instance, and `/path/to/destination` with the path to the directory where you want to store the Flask application files on the EC2 instance
   
2. Install the required Python packages on the EC2 instance

   - SSH into the EC2 instance: `ssh -i /path/to/key.pem ec2-user@<ec2-instance-public-ip>`
   - Navigate to the directory where you copied the Flask application files
   - Install the required Python packages using pip: `sudo pip install -r requirements.txt`
   
3. Run the Flask application on the EC2 instance

   - Start the Flask application using the following command:
   ````
   nohup python app.py > /dev/null 2>&1 &
   ```
   - This command starts the Flask application in the background and redirects all output to `/dev/null` so that it doesn't clutter the console output
   - Note the URL where the Flask application is running (usually `http://localhost:5000` by default)
   - You can verify that the Flask application is running by navigating to the URL in your web browser
   
4. Configure the EC2 instance security group

   - In the AWS Management Console, navigate to the EC2 service
   - Select your EC2 instance and click the "Actions" button
   - Choose "Networking" and then "Change Security Groups"
   - Add a new inbound rule to allow incoming traffic on port 5000 (or whichever port your Flask application is running on)
   - You can restrict the source IP addresses to only allow traffic from certain IP ranges if desired
   
5. Test the deployed Flask application

   - Navigate to the URL of your EC2 instance in your web browser, using the public IP address or DNS name of the instance
   - Upload an input image file and click the "Remove Background" button
   - Verify that the output image is displayed on the web page
   
Congratulations! You have successfully deployed a Flask application that removes the background from an image to an EC2 instance on AWS.

Note that the steps above are just a basic guide to get you started. You may need to modify some of the steps or add additional configuration depending on the specific requirements of your Flask application. For example, you may need to configure a web server like Nginx or Apache to serve the Flask application, or set up a domain name using Route 53. Be sure to consult the AWS documentation for more information.
