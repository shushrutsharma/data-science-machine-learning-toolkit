from bs4 import BeautifulSoup
import requests
import time

print('Put some skills you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')





def find_jobs():

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date= job.find('span', class_='sim-posted').span.text

        if 'few' in published_date:

            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill.capitalize and unfamiliar_skill.lower and unfamiliar_skill not in skills:
                with open(f'./posts/{index}.txt', 'w') as f:
                    f.write("\n")
                    f.write(f'''comany name : {company_name.strip()}
requires : {skills.strip()}
publised : {published_date}''')

                    f.write(f'More Info : {more_info}')
                    f.write ("\n")
                    f.write('-----------------------------------')
                print(f'File saved : {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds....')
        time.sleep(time_wait*6)
