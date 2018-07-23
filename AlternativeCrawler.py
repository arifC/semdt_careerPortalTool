import scrapy

job_urls = ['https://www.bmwgroup.com/de/karriere/job-description.DE_122340.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_120209.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_122697.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_122030.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_122524.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_122237.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_122302.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_122658.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_122474.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_122475.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_120979.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_122289.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_122532.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_121056.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_121876.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_121697.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_119873.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_119463.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_120322.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_119786.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_119066.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_117545.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_117545.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_117177.DE.Munich.InformationTechnology.ITProjectManagement.html',
            'https://www.bmwgroup.com/de/karriere/job-description.DE_116480.DE.Munich.InformationTechnology.ITProjectManagement.html']

for page in job_urls:
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    for row in soup.html.body.findAll('tr'):
        data = row.findAll('td')
        if data and 'subclass 885online' in data[0].text:
            print(data[4].text)