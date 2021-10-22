# End of life OS - Web Scraping using Scrapy and Data Ingestion Into Splunk for analytics/reporting

Containerized application using Scrappy to scrape OS vendor websites namely - Ubuntu, CentOS, RHEL, Windows, to fetch EOL dates for different versions of OS and ingests this data into Splunk. This data can be used to compare with existing OS versions for systems in the environment to find systems running EOL OS.

## Executing the script

1. Git clone this repo.

```bash
$ git clone https://github.com/radpai/End-Of-Life-OS
```

2. Create .credentials.env in the directory and add following :

SPLUNK_INDEX=<splunk_index>  
SPLUNK_SOURCE=<splunk_source>  
SPLUNK_URL=<splunk_url_endpoint>  
SPLUNK_TOKEN=<splunk_token>  

3. Build and run the container

```bash
$ docker-compose --env-file .credentials.env up --build
```

On completion, the data will be ingested into Splunk. 

In Splunk check for the data by executing a Splunk query and check for the interesting fields.

```splunk
index=<splunk_index> source=<splunk_source>
```

Use this data to create interesting views by correlating and comparing with existing OS versions for systems in the environment to find systems running EOL OS.
