import requests
from bs4 import BeautifulSoup

class MatchParser:
    URL = None

    def __init__(self, league):
        self.HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:86.0) Gecko/20100101 Firefox/86.0',
            'accept': '*/*' }

        if league.upper() == 'АПЛ':
            self.URL = 'https://www.google.ru/search?newwindow=1&source=hp&ei=KcJMYPOyMY6nUunNj7AK&iflsig=AINFCbYAAAAAYEzQOeQpAzDxHee1f7V1-pAfu1PME-MS&q=epl&oq=epl&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAELEDMgUIABCxAzICCAAyAggAMgIIADILCAAQsQMQxwEQowIyBQgAELEDMgIIADILCAAQsQMQxwEQowIyBQgAELEDOggIABCxAxCDAToICC4QsQMQgwE6BQguELEDOgYIABAKEAE6AgguOggIABDHARCjAjoICAAQxwEQrwE6BAgAEApQlwtY1CpgpCxoA3AAeACAAWqIAZsFkgEDNS4ymAEAoAEBqgEHZ3dzLXdperABAA&sclient=gws-wiz&ved=0ahUKEwiz68nts63vAhWOkxQKHenmA6YQ4dUDCAY&uact=5'
        elif league.upper() == 'СЕРИЯ А':
            self.URL = 'https://www.google.ru/search?newwindow=1&source=hp&ei=BzFOYIy_E6qHrwSXurbYBA&iflsig=AINFCbYAAAAAYE4_FysGqlb725GeEcJiOyX97X4hXe29&q=seria+a&oq=seria+a&gs_lcp=Cgdnd3Mtd2l6EAMyDQguELEDEIMBEAoQkwIyBAgAEAoyCggAELEDEIMBEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAo6CAgAELEDEIMBOgsIABCxAxDHARCjAjoFCAAQsQM6AggAOgUILhCxAzoICC4QsQMQgwE6AgguOggIABDHARCvAToICC4QsQMQkwI6CgguELEDEIMBEAo6BwgAELEDEApQvxFY_TRggjZoA3AAeACAAW-IAZMGkgEDNS4zmAEAoAEBqgEHZ3dzLXdperABAA&sclient=gws-wiz&ved=0ahUKEwjM3vfckbDvAhWqw4sKHRedDUsQ4dUDCAY&uact=5'
        elif league.upper() == 'БУНДЕСЛИГА':
            self.URL = 'https://www.google.ru/search?newwindow=1&ei=DjFOYKinOO-GrwTC-6GYCw&q=bundesliga&gs_ssp=eJzj4tTP1TcwNjc0szRg9OJKKs1LSS3OyUxPBABGIwa8&oq=seria+a&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCC4QsAMQQxCTAjIHCC4QsAMQQzIHCC4QsAMQQzIHCAAQsAMQQzIJCC4QsAMQChBDMgcILhCwAxBDMgcILhCwAxBDMgcILhCwAxBDMgcILhCwAxBDMgcILhCwAxBDUABYAGCQ0y9oAXABeACAAW-IAW-SAQMwLjGYAQCqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz'
        elif league.upper() == 'ЛИГА 1':
            self.URL = 'https://www.google.ru/search?newwindow=1&ei=HTROYIbdH_GkrgS21I4I&q=ligue+1&gs_ssp=eJzj4tTP1TcwMcmoyDFg9GLPyUwvTVUwBAA64QWs&oq=li&gs_lcp=Cgdnd3Mtd2l6EAMYATIHCC4QQxCTAjIECC4QQzIECAAQQzIECAAQQzIECC4QQzIECAAQQzIECC4QQzIECC4QQzIECC4QQzIECC4QQzoKCC4QsAMQQxCTAjoHCC4QsAMQQzoHCAAQsAMQQ1CljAVYko4FYJObBWgBcAJ4AYAB_AeIAYoLkgEJMC4xLjEuNy0xmAEAoAEBqgEHZ3dzLXdpesgBCsABAQ&sclient=gws-wiz'
        elif league.upper() == 'ЛА ЛИГА':
            self.URL = 'https://www.google.ru/search?newwindow=1&ei=dDROYIjPJufnrgT2o4i4AQ&q=la+liga&gs_ssp=eJzj4tDP1TewTC-sMGD0Ys9JVMjJTE8EADYDBaM&oq=la+&gs_lcp=Cgdnd3Mtd2l6EAMYADINCC4QsQMQgwEQQxCTAjIECC4QQzIFCAAQsQMyCggAEMcBEK8BEEMyCggAEMcBEKMCEEMyCwgAELEDEMcBEKMCMgUIABCxAzIECAAQQzIICC4QsQMQgwEyCggAELEDEIMBEEM6CgguELADEEMQkwI6BwguELADEEM6BwgAELADEENQ3vYBWKv4AWCMgQJoAXACeAKAAeAFiAGMDZIBCTAuMi41LTEuMZgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz'

    def __get_html(self, url):
        request = requests.get(url, headers=self.HEADERS)
        return request

    def parse(self):
        html = self.__get_html(self.URL)

        if html.status_code == 200:
            soup = BeautifulSoup(html.content, 'html.parser')
            tables = soup.findAll('table', {'class': 'KAIX8d'})

            matches = []
            for table in tables:
                teams = []
                date_time = {
                    'date': None,
                    'time': None,
                }

                teams_html = table.findAll('div', {'class':'ellipsisize kno-fb-ctx'})
                date_time_html = table.findAll('div', {'class': 'imspo_mt__ns-pm-s'})

                for team in teams_html:
                    teams.append(team.text)

                for date_time in date_time_html:
                    date_time['date'] = date_time.find('div', {'class': 'imspo_mt__pm-inf imspo_mt__pm-infc imspo_mt__date imso-medium-font'}).text
                    date_time['time'] = date_time.find('div', {'class': 'imspo_mt__ndl-p imspo_mt__pm-inf imspo_mt__pm-infc imso-medium-font'}).text

                matches.append({
                    'teams': teams,
                    'date': date_time['date'],
                    'time': date_time['time'],
                })

            return matches

        else:
            print('Error')


if __name__ == '__main__':
    matchParser = MatchParser('СЕРИЯ А')
    matches = matchParser.parse()
    print(matches)
