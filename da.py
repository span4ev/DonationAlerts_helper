from bs4 import BeautifulSoup
import shutil, random, locale, math, sys, os

# Локаль для правильной сортировки русских букв
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

class DA:

    def __init__(self, 
                 script_option, 
                 sorting, 
                 min_donation_sum, 
                 donations_lines_amount, 
                 total_sum, 
                 line_ending, 
                 show_donation_date):

        self.open_file_summation    = 'donations.txt'
        self.output_file_summation  = '_DONATION_SUMMATION_RESULT_.txt'

        self.folder_path_html       = '.'
        self.open_file_html         = ''
        self.output_file_html       = '_FULL_DOTATIONS_INFO_.txt'

        self.script_option          = int(script_option)
        self.sorting                = int(sorting)
        self.min_donation_sum       = int(min_donation_sum)
        self.donations_lines_amount = int(donations_lines_amount)
        self.total_sum              = int(total_sum)
        self.line_ending            = str(line_ending)
        self.show_donation_date     = int(show_donation_date)

        self.donations_lines        = []
        self.donations_full_info    = []

        self.trash_html_text_1 = '<li><span class="username">'
        self.trash_html_text_2 = '</span><span class="delimiter"> - </span><span class="amount">'
        self.trash_html_text_3 = ' <span class="currency">RUB</span></span></li>'
        self.generate_donates_html_first_line = '<ul class="da-donationslist">'
        self.generate_donates_html_line = '</ul>'

        self.html_donations_inner_ = 'b-last-events-widget__item--inner'
        self.html_date_            = 'date-container action-date-container unselectable'
        self.html_nickname_        = '_name'
        self.html_money_           = '_sum'
        self.html_message_         = 'message-container b-last-events-widget__item--text'
        self.html_video_name_      = 'action-button-item__sign'
        self.html_video_url_       = 'action-button-item'
        self.html_commission_      = 'commission-covered-icon'

        self.html_heart            = ' ♥ '
        self.html_commission_text  = 'Этот пользователь покрыл комиссию сервиса и платёжной системы'
        self.html_subscribe_text   = 'подписался на канал Twitch!'

        self.total_sum_text = 'Общая сумма -'


    def find_and_rename_latest_donations_file(self):

        max_ctime = 0
        latest_file_name = None

        files = [file for file in os.listdir() if 'donations' in file and file.endswith('.txt')]

        if files:

            for file in files:
                file_ctime = os.path.getctime(file)
                if file_ctime > max_ctime:
                    max_ctime = file_ctime
                    latest_file_name = file

            for file in files:
                if file != latest_file_name and len(files) > 1:
                    if os.path.exists(file):
                        os.remove(file)

            if latest_file_name:
                os.rename(latest_file_name, self.open_file_summation)

    def get_donations_lines(self):

        temp_lst = []
        temp_dict = {}

        if os.path.exists(self.open_file_summation):
            with open (self.open_file_summation, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if '\ufeff' in lines[0]:
                    lines[0] = lines[0].replace('\ufeff', '')

        if lines:
            for i in lines:
                split = i.split(self.trash_html_text_1)
                if len(split) > 1:
                    x = split[-1].split(self.trash_html_text_2)
                    y = x[1].split(self.trash_html_text_3)[0]
                    temp_lst.append((x[0], y))


        for i in temp_lst:
            x, y = i[0], i[1]

            if ' ' in y:
                y = y.replace(' ', '')

            if ',' in y:
                y = y.replace(',', '.')
                y = float(y)
                y = math.ceil(y)

            y = int(y)

            if not x in temp_dict:
                temp_dict[x] = y
            else:
                temp_dict[x] += y

        for i, k in temp_dict.items():   
            self.donations_lines.append((i, k))

    def sorting_lines(self):

        lst = self.donations_lines

        if lst:
            if self.sorting == 1:
                lst = lst
            if self.sorting == 2:
                lst = lst[::-1]
            if self.sorting == 3:
                lst = [(t[1], t[0]) for t in lst]
                lst = sorted(lst, key=lambda x: x[0], reverse=True)
                lst = [(t[1], t[0]) for t in lst]
            if self.sorting == 4:
                lst = [(t[1], t[0]) for t in lst]
                lst = sorted(lst, key=lambda x: x[0])
                lst = [(t[1], t[0]) for t in lst]
            if self.sorting == 5:
                lst = sorted(lst, key=lambda item: item[0].lower())

        self.donations_lines = lst

    def write_result(self):

        lst = self.donations_lines

        result_sum = sum(int(i[1]) for i in lst)
        min_donation_sum_lst = []

        with open (self.output_file_summation, 'w', encoding='utf-8') as f:

            if self.min_donation_sum:
                for i in lst:
                    if i[1] >= self.min_donation_sum:
                        min_donation_sum_lst.append(i)

                lst = min_donation_sum_lst

            for i in lst:
                result_sum += int(i[1])

            for i in lst[:self.donations_lines_amount] if self.donations_lines_amount > 0 else lst:
                line = f'{i[0]} - {i[1]} {self.line_ending} \n'
                f.writelines(line)

            if self.total_sum:
                pass
                f.write(f'\n{self.total_sum_text} {result_sum} {self.line_ending}')

    def read_html(self):

        folder_to_delete  = ''
        result = []

        for file in os.listdir(self.folder_path_html):
            if file.endswith('.html'):
                self.open_file_html = file


        if os.path.exists(self.open_file_html):
            if self.open_file_html.replace('.html', '') in file and '_files' in file:
                folder_to_delete = file
                shutil.rmtree(folder_to_delete)

            with open(self.open_file_html, 'r', encoding='utf-8') as f:
                html = f.read()

            soup = BeautifulSoup(html, 'html.parser')
            self.donations_full_info = soup.find_all('div', class_= self.html_donations_inner_)

        if self.donations_full_info:
            for i in self.donations_full_info:

                date        = i.find('span', class_ = self.html_date_)
                nickname    = i.find('span', class_ = self.html_nickname_)
                money       = i.find('span', class_ = self.html_money_)
                message     = i.find('div',  class_ = self.html_message_)
                video_name  = i.find('span', class_ = self.html_video_name_)
                video_url   = i.find('a',    class_ = self.html_video_url_)

                date        = date.get_text().strip()       if date else ''
                nickname    = nickname.get_text().strip()   if nickname else ''
                money       = money.get_text().strip()      if money else ''
                message     = message.get_text().strip()    if message != None else ''
                video_name  = video_name.get_text().strip() if video_name != None else ''
                video_url   = video_url['href'].strip()     if video_url else ''

                img_tag = i.find('img', class_= self.html_commission_)
                
                commission_covered = False
                
                if img_tag and self.html_commission_text in img_tag['title']:
                    commission_covered = True

                if money:
                    x = f'({date})\n{nickname} : {money}' if self.show_donation_date else f'{nickname} : {money}'
                    if commission_covered:
                        x += self.html_heart
                else:
                    x = f'({date})\n{nickname} : {self.html_subscribe_text}' if self.show_donation_date else f'{nickname} : {self.html_subscribe_text}'


                if message:
                    x += f'\n— {message}'
                if video_name:
                    x += f'\n«{video_name}»'
                if video_url:
                    x += f'\n{video_url}'
                x += '\n'

                result.append(x)

            with open(self.output_file_html, 'w', encoding='utf-8') as f:
                for i in result:
                    f.write(f'{i}\n')



        

    def start(self):

        if self.script_option == 1:
            self.find_and_rename_latest_donations_file()
            self.get_donations_lines()
            self.sorting_lines()
            self.write_result()

        if self.script_option == 2:
            self.read_html()
