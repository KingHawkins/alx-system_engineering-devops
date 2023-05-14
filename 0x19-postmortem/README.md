<h1>Postmortem</h1>

<h2>Issue Summary:</h2>
On May 13th, 2023, from 2:00 PM to 5:00 PM (UTC-5), our web application experienced an outage that affected 75% of our users. Users were unable to access our website, and those who were already logged in experienced slow response times.

<h2>Timeline:</h2>

<h4>2:00 PM:</h4> The issue was detected when a monitoring alert was triggered due to high server CPU usage.
<h4>2:01 PM:</h4> The engineering team was notified of the issue, and they immediately started investigating the problem.
<h4>2:05 PM:</h4> The team noticed that the database server was running slow and suspected it to be the root cause of the issue.
<h4>2:15 PM:</h4> The team started investigating the database server, but they found no issues with it.
<h4>2:30 PM:</h4> The team started investigating other parts of the system, such as load balancers and caching servers, but they found no issues.
<h4>3:00 PM:</h4> The team realized that the issue was caused by a misconfigured firewall rule that was blocking incoming traffic to the web application servers.
<h4>3:30 PM:</h4> The team corrected the misconfigured firewall rule, and the issue was resolved.
<h4>4:00 PM:</h4> The engineering team notified the customer support team that the issue had been resolved.
<h4>5:00 PM:</h4> The incident was officially closed.
<h2>Root Cause and Resolution:</h2>
The root cause of the issue was a misconfigured firewall rule that was blocking incoming traffic to the web application servers. This caused a bottleneck that slowed down the system and eventually led to the outage.

To fix the issue, the engineering team corrected the misconfigured firewall rule, allowing traffic to flow normally to the web application servers. After the correction was made, the system returned to normal operating conditions.

<h2>Corrective and Preventative Measures:</h2>
To prevent similar incidents in the future, the engineering team will implement the following corrective and preventative measures:

Implement automated monitoring to detect misconfigured firewall rules.
Develop and implement a protocol for verifying the correctness of firewall rules before deployment.
Develop and implement a disaster recovery plan to ensure business continuity in case of a similar outage.
Tasks to address the issue:

Implement automated monitoring to detect misconfigured firewall rules. (Task assigned to DevOps team, deadline: 2 weeks)
Develop and implement a protocol for verifying the correctness of firewall rules before deployment. (Task assigned to Network Engineering team, deadline: 1 month)
Develop and implement a disaster recovery plan to ensure business continuity in case of a similar outage. (Task assigned to System Engineering team, deadline: 3 months)
In conclusion, the outage on May 13th, 2023, was caused by a misconfigured firewall rule that was blocking incoming traffic to the web application servers. The issue was resolved in a timely manner, and corrective and preventative measures were put in place to prevent similar incidents in the future.
