import pprint
import urllib.request
import json
import codecs

with urllib.request.urlopen("https://www.bmwgroup.com/de/karriere/_jcr_content/par/jobfinder.joblist.de.json") as url:
    dataJobs = json.loads(url.read().decode('utf-8'))

with urllib.request.urlopen("https://www.bmwgroup.com/de/karriere/_jcr_content/par/jobfinder.joblist-search.de.json") as url:
    dataDescriptions = json.loads(url.read().decode('utf-8'))

bmw_refNo = ['DE_122931']

def get_description_text(ref):
    description = ""
    for job in dataDescriptions['data']:
        if job['refNo'] == ref:
            description = json.dumps(job['fulltext'], indent=4, sort_keys=True)

    return description

def get_job_details(refArray):
    for refNo in refArray:
        for job in dataJobs['data']:
            if job['refNo'] == refNo:
                print(json.dumps(job, indent=4, sort_keys=True))
                print(get_description_text(refNo))

#get_job_details(bmw_refNo)

text_file = codecs.open("bmw_desc.txt", "w", "utf-8")
text = ""

for desc in dataDescriptions['data']:
    desc = json.dumps(desc, indent=4, sort_keys=True, ensure_ascii=False).split('Ansprechpartner:')[0]
    print(desc)
    if ("the" not in desc) and ("degree" not in desc) and ("about" not in desc):
        text += desc

text_file.write(text)
text_file.close()