# Setting up AWS CLI

It is recommended to use Windows Terminal, which can be installed via the Microsoft Store.

Download the AWS CLI from: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
After installing you can check whether the installtion was successful by opening a new terminal and typing 'aws --version'.

Reminder: If you had the terminal open before installing the AWS CLI you need to close and open a new one.

It should output something like this:

aws-cli/2.4.5 Python/3.8.8 Windows/10 exe/AMD64 prompt/off


After that has been setup and you see the above output, you need to configure you profile.
In order to do that use 'aws configure'.
It will ask for your id and key which you will get from our admin.
For the region you input eu-central-1 and for default output use yaml.

To check your setup you can try the 'aws ecr describe-repositories' command.
You should get an output of all repositories e.g. ''simplic-oxs-contact'.

