import subprocess
import os
import wget
import tarfile 

# Update packages
#subprocess.run(["pip", "install", "--upgrade", "pip"])

# Install OpenJDK 8
#clsubprocess.run(["apt-get", "install", "openjdk-8-jdk-headless", "-qq"])

# Download Spark
url = "https://downloads.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz"
filename = "spark-3.4.0-bin-hadoop3.tgz"
wget.download(url, filename)

print("checkpoint1")
# Extract Spark
try:
    with tarfile.open(filename, "r:gz") as tar:
        tar.extractall()
except tarfile.ReadError:
    print("Failed to extract the tar file. Make sure the downloaded file is not corrupted.")


# Install findspark
os.system("pip install findspark")

print("checkpoint1")

# Set environment variables
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "./spark-3.4.0-bin-hadoop3"

# Initialize findspark
import findspark
findspark.init()

print("checkpoint1")



