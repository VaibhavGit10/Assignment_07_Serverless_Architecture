## ⚙️ Graded Assignment: Serverless Architecture with AWS Lambda & Boto3

Welcome to the Serverless Automation Tasks repository! This project demonstrates real-world DevOps use cases implemented using AWS Lambda and Boto3, showcasing how serverless functions can be used to manage and automate various AWS services such as EC2, S3, and more.

Each task is encapsulated in a Lambda function (lambda_function.py), featuring concise and practical automation logic. These implementations are designed to simulate production-like scenarios in cloud infrastructure management, with a strong emphasis on:

- ✅ Automation Efficiency

- ☁️ Serverless Design Principles

- Event-Driven Architecture

- 🔐 IAM Security and Permissions

- 🧰 Boto3 SDK Usage for AWS Service Integration


## 📂 Structure Overview

```text
📂 Q01/ -> Task 01: Auto EC2 Management
└── lambda_function.py

📂 Q02/ -> Task 02: S3 Bucket Cleanup
└── lambda_function.py

📂 Q03/ -> Task 03: Unencrypted S3 Monitor
├── lambda_function.py

📂 Q05/ -> Task 05: Auto-Tag EC2 on Launch
└── lambda_function.py

📂 Q17/ -> Task 17: Restore EC2 from Snapshot
├── lambda_function.py

```

---

## 🧪 Task 01: Automated EC2 Instance Management Using Tags

📁 Directory: Q1

📜 Script: lambda_function.py

## ✅ Objective

-Automate the start and stop actions of EC2 instances based on custom tag values using an AWS Lambda function.

## ⚙️ How It Works
This Lambda function scans EC2 instances in the account and performs the following:

🔹 🚀 Start Instances with the tag:
Action = Auto-Start

🔹🛑 Stop Instances with the tag:
Action = Auto-Stop

🔹📝 Logging:
The function logs all affected instance IDs for auditing and troubleshooting.

## 📌 Use Case
This task demonstrates a real-world approach to managing EC2 resources efficiently using tags, helping reduce manual effort and optimize cloud costs through automated scheduling logic.


### 📸 Screenshots:

![Img_01_Q1](https://github.com/user-attachments/assets/52e8eba5-adbe-4980-88a9-450fc3be9ca8)
![Img_02_Q1](https://github.com/user-attachments/assets/a2b3e6b6-ac1d-486d-ad01-c51ae4bebf29)
![Img_03_Q1](https://github.com/user-attachments/assets/b4927007-608f-42dd-a753-3d5f0984830e)
![Img_04_Q1](https://github.com/user-attachments/assets/4d6d9305-8abf-4644-8c2e-0abf1ccb66da)
![Img_05_Q1](https://github.com/user-attachments/assets/50470ec0-153e-4f41-9090-0e90067380e5)
![Img_06_Q1](https://github.com/user-attachments/assets/d3ab05fb-a866-4ddb-8862-b015ec2271dc)
![Img_07_Q1](https://github.com/user-attachments/assets/ceed2ebc-8540-4483-b3e4-f6fffa5dc58d)
![Img_08_Q1](https://github.com/user-attachments/assets/17bf1f3c-3df3-4ac1-bd23-c13b1fee9cd4)
![Img_09_Q1](https://github.com/user-attachments/assets/862c1ff0-2ff4-4dfa-82de-f96721156f1a)
![Img_10_Q1](https://github.com/user-attachments/assets/06a3121b-4b9b-4848-8e25-671381c93daf)
![Img_11_Q1](https://github.com/user-attachments/assets/18ece3b5-b089-46c6-b62c-00a1bafb3dcb)
![Img_12_Q1](https://github.com/user-attachments/assets/74e1df93-5652-4c26-94ef-ab8fca31e479)
![Img_13_Q1](https://github.com/user-attachments/assets/2422cdd3-80d9-4a05-8ba4-d8799b7494d3)
![Img_14_Q1](https://github.com/user-attachments/assets/bea1673b-b8a0-4deb-89dd-5de26d66ac09)
![Img_15_Q1](https://github.com/user-attachments/assets/3a720821-d9d7-480a-8aa4-b1ce553784c6)
![Img_16_Q1](https://github.com/user-attachments/assets/91b5d7a6-c718-44cc-be6a-8b907af24014)

---

## 🧪 Task 02: Automated S3 Bucket Cleanup

- 📁 Directory: `Q2`
- 📜 Script: `lambda_function.py`

### ✅ Objective

Automatically clean up outdated files in an S3 bucket to manage storage usage and maintain data hygiene.

## ⚙️ How It Works

This Lambda function performs the following steps:
- 📄 Lists all objects in the specified S3 bucket
- ⏳ Identifies and deletes files older than a specified threshold (default: 30 days). For testing we used the time to 1 or 2 days.
- 📝 Logs the deleted file names for visibility, auditing, and debugging purposes

## 📌 Use Case

This task represents a common serverless pattern for data lifecycle management, helping ensure that old and unnecessary data does not accumulate in object storage, reducing costs and clutter.



### 📸 Screenshots:

![Q2_Img_01](https://github.com/user-attachments/assets/17aab529-f892-406f-a945-bad7739f1a80)
![Q2_Img_02](https://github.com/user-attachments/assets/a4258bf7-aca2-4979-a9c2-30939af3a92c)
![Q2_Img_03](https://github.com/user-attachments/assets/221a65d5-fe0d-447a-8485-fd8490b19916)
![Q2_Img_04](https://github.com/user-attachments/assets/fd2e6859-08ac-42c4-a01b-e092b57b4d7b)
![Q2_Img_05](https://github.com/user-attachments/assets/f6f3a3ba-a810-4fa7-9a92-8621c21e60c9)
![Q2_Img_06](https://github.com/user-attachments/assets/a612085a-bba9-46a5-b775-8ed3297e4abc)
![Q2_Img_07](https://github.com/user-attachments/assets/057fe0b9-3c19-4f84-a9d5-f9db5dc3e8fa)
![Q2_Img_08](https://github.com/user-attachments/assets/ae065cbe-8744-4a85-8a43-c76228e848f6)
![Q2_Img_09](https://github.com/user-attachments/assets/68f38972-1da6-4e6d-bad6-bd10c004635e)
![Q2_Img_10](https://github.com/user-attachments/assets/c8e6aaf1-584e-4812-b34e-c1d01ce73b9d)
![Q2_Img_11](https://github.com/user-attachments/assets/113d8ef2-a79e-4887-8354-f54a870fd8df)
![Q2_Img_12](https://github.com/user-attachments/assets/f47d6048-0ab1-42e5-8493-5b7ca7f28521)

---

## 🧪 Task 03: Monitor Unencrypted S3 Buckets

- 📁 Directory: `Q3`
- 📜 Script: `lambda_function.py`

## ✅ Objective

Enhance cloud security by identifying and reporting S3 buckets that do not have server-side encryption (SSE) enabled.

## ⚙️ How It Works
This Lambda function performs the following:

- 🪣 Lists all available S3 buckets in the AWS account

- 🔍 Inspects bucket encryption settings to detect lack of SSE

- 🛑 Flags and logs unencrypted buckets for immediate attention


## ⚠️ Important Note

The AWS account used for testing had default encryption policies enabled, which prevented the creation of unencrypted S3 buckets.
As a result, the detection logic for unencrypted buckets was implemented but could not be fully tested in a live environment.

### 📸 Screenshots:

![Q3_Img_01](https://github.com/user-attachments/assets/bfce1fd6-819a-4625-9d42-e25a67a2329d)
![Q3_Img_02](https://github.com/user-attachments/assets/13ae40dd-10b1-4f03-95d7-672f8680e54c)
![Q3_Img_03](https://github.com/user-attachments/assets/621f11db-e088-4a6c-afab-88d417584a96)
![Q3_Img_04](https://github.com/user-attachments/assets/e2b81b69-8f06-482b-b1e8-77fee6772c44)
![Q3_Img_05](https://github.com/user-attachments/assets/2986d3c0-3e5d-4379-91d3-a1b564d23b04)
![Q3_Img_06](https://github.com/user-attachments/assets/f5185528-2650-4000-98ce-082258907756)
![Q3_Img_07](https://github.com/user-attachments/assets/a8c9e71f-c99a-4d37-af0f-202f0cf4736a)
![Q3_Img_08](https://github.com/user-attachments/assets/0f81dba6-57dc-4b70-9f02-f649dab7aeb2)
![Q3_Img_09](https://github.com/user-attachments/assets/b468f6dd-246b-427a-9880-e4ee4be791f2)
![Q3_Img_10](https://github.com/user-attachments/assets/0609a658-87f2-481a-9e0c-11a19cbf033c)


---

## 🏷️ Task 05: Auto-Tag EC2 Instances on Launch

- 📁 Directory: `Q5`
- 📜 Script: `lambda_function.py`

### ✅ Objective
Automatically tag newly launched EC2 instances with useful metadata to enhance resource visibility, cost tracking, and governance.

## ⚙️ How It Works
This Lambda function is triggered via **CloudWatch Events (EventBridge)** whenever a new EC2 instance is launched:

- 🆔 **Extracts the instance ID** from the launch event payload

- 🏷️ **Applies metadata tags** to the instance:

-- `LaunchDate`: Current system date (acts as a timestamp)
-- `Environment`: A custom tag (e.g., `"Dev", "Staging", "Prod"`)

## 📌 Use Case
Tagging is a critical best practice in cloud management. This automation helps organizations:

- 📊 Track resource usage by environment

- 💰 Allocate costs accurately

- 🔍 Improve auditing and operational insights

- 🔒 Enforce tagging policies consistently


### 📸 Screenshots:

![Q5_Img_01](https://github.com/user-attachments/assets/5e09ec3d-c090-4a52-8126-591dfaed231b)
![Q5_Img_02](https://github.com/user-attachments/assets/cf93ce1e-fc3c-4a83-98da-5a3ebfe9221a)
![Q5_Img_03](https://github.com/user-attachments/assets/56538b97-6c9b-46d9-bb65-d646f7d608d0)
![Q5_Img_04](https://github.com/user-attachments/assets/971e290a-8a62-4584-94e9-a05ca18a7dbe)
![Q5_Img_05](https://github.com/user-attachments/assets/9fb67065-bd0f-4a7d-99bc-7ac5e5bb83c4)
![Q5_Img_06](https://github.com/user-attachments/assets/3f56f935-d349-436f-b5ba-95f6b8b0fa08)
![Q5_Img_07](https://github.com/user-attachments/assets/7f6a5298-9160-44c7-80a6-692d34f503ad)
![Q5_Img_08](https://github.com/user-attachments/assets/16713a21-842e-49ab-9221-df9cfe6c2fa6)
![Q5_Img_09](https://github.com/user-attachments/assets/5d2f78ed-37da-4e9c-b9f6-514261c3931b)
![Q5_Img_10](https://github.com/user-attachments/assets/3ec8cc4c-5e72-470a-8554-067628f6e299)
![Q5_Img_11](https://github.com/user-attachments/assets/8fa15d6f-e6f3-486d-a494-0faac497c76a)
![Q5_Img_12](https://github.com/user-attachments/assets/523e0b32-71b0-4381-b77d-ccdf65846383)

---

## 🧪 Task 17: Restore EC2 Instance from Snapshot

- 📁 Directory: `Q17`
- 📜 Script: `lambda_function.py`
- 📄 IAM Policy File: `JL-EC2-Restore-Policy.json`

### ✅ Objective
Automate the process of restoring an EC2 instance from the latest snapshot, enabling fast recovery or environment duplication.

### ⚙️ How It Works
This Lambda function performs the following steps:

1. 🔍 Scans and filters snapshots based on predefined tags or criteria

2. 🕓 Selects the most recent snapshot (by creation date)

3. 💽 Creates a new EBS volume from the selected snapshot

4. 🚀 Launches a new EC2 instance with the restored volume attached

5. 📝 Logs the instance ID of the newly launched EC2 instance for tracking

### 📌 Use Case

This solution is ideal for:

- 🆘 Disaster Recovery scenarios

- 🧪 Scheduled Restore Testing to validate backups

- 🧬 Environment Cloning for dev/test from production snapshots

---

### 📸 Screenshots:

![Q17_01](https://github.com/JOYSTON-LEWIS/My-Media-Repository/blob/main/Assignment_07_DevOps_Outputs_Images/Q17_01.png)
![Q17_02](https://github.com/JOYSTON-LEWIS/My-Media-Repository/blob/main/Assignment_07_DevOps_Outputs_Images/Q17_02.png)
![Q17_03](https://github.com/JOYSTON-LEWIS/My-Media-Repository/blob/main/Assignment_07_DevOps_Outputs_Images/Q17_03.png)
![Q17_04](https://github.com/JOYSTON-LEWIS/My-Media-Repository/blob/main/Assignment_07_DevOps_Outputs_Images/Q17_04.png)
![Q17_05](https://github.com/JOYSTON-LEWIS/My-Media-Repository/blob/main/Assignment_07_DevOps_Outputs_Images/Q17_05.png)
![Q17_06](https://github.com/JOYSTON-LEWIS/My-Media-Repository/blob/main/Assignment_07_DevOps_Outputs_Images/Q17_06.png)
![Q17_07](https://github.com/JOYSTON-LEWIS/My-Media-Repository/blob/main/Assignment_07_DevOps_Outputs_Images/Q17_07.png)
![Q17_08](https://github.com/JOYSTON-LEWIS/My-Media-Repository/blob/main/Assignment_07_DevOps_Outputs_Images/Q17_08.png)
![Q17_09](https://github.com/JOYSTON-LEWIS/My-Media-Repository/blob/main/Assignment_07_DevOps_Outputs_Images/Q17_09.png)
![Q17_10](https://github.com/JOYSTON-LEWIS/My-Media-Repository/blob/main/Assignment_07_DevOps_Outputs_Images/Q17_10.png)

---

### 🚀 Upcoming Updates

- ✅ 5 out of 19 serverless tasks from the assignment have been completed and added to this repository.
- 🛠️ More solutions are actively under development and will be uploaded soon!
- 📘 Each task is designed to demonstrate a real-world use case using AWS Lambda + Boto3, with clean code and detailed logging.
- 🔁 This repository will continue to evolve with new tasks, improvements, and best practices over time.

### 📜 License

This project is licensed under the MIT License.
You're free to use, copy, modify, and share the scripts as you wish — just give credit where it's due.

### 🤝 Contributing

Have ideas to enhance these automations or want to fix something? Contributions are highly encouraged!
Here's how you can contribute:

- 🍴 Fork this repository

- 💡 Add new features or improvements

- ✅ Test thoroughly

- 📩 Submit a pull request

If you like this project or find it useful, **please consider giving it a ⭐ on GitHub** — it really helps boost visibility and encourages further open-source development. 🙌


🎯 Thank you for visiting this project!
I hope it helps you learn, build, and automate better with AWS Lambda + Boto3.
