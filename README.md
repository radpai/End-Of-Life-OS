# End of life OS - Web Scraping using Scrapy and Data Ingestion Into Splunk for analytics/reporting

1. Git clone this repo
2. Create .credentials.env in the directory and add following :
   
   SPLUNK_INDEX=<splunk_index>
   SPLUNK_SOURCE=<splunk_source>
   SPLUNK_URL=<splunk_url_endpoint>
   SPLUNK_TOKEN=<splunk_token>
   
3. Run following to build and run your application container .
   docker-compose --env-file .credentials.env up --build
