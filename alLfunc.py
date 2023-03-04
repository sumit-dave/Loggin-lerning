import logging

class listt:
    def __init__(self, data1):
        import logging
        logging.basicConfig(filename='test1.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
        logging.info('List module executed')
        self.data=data1

    def extract_list(self):
        '''try to extract all the list entity'''
        try:
            for i in self.data:
                if type(i) == list:
                    logging.info(i)
        except Exception as e:
            logging.exception(e)


    def extract_dict(self):
        '''try to extract dict entity'''
        try:
            for i in self.data:
                if type(i) == dict:
                    logging.info(i)
        except Exception as e:
            logging.exception(e)


    def all_numeric_data(self):
        '''try to extract numeric data only form the list'''
        try:
            num = []
            for i in self.data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            num.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            num.append(k)
                            num.append(v)
                else:
                    num.append(i)
            logging.info('all numeric values are %s',num)
            logging.info('all numeric values submmtion is %s',sum(num))
        except Exception as e:
            logging.exception(e)

    def all_odd_values(self):
        '''try to pull up all add numeric values from the list'''
        try:
            odd_num = []
            for i in self.data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int and j%2==1:
                            odd_num.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int and k%2==1:
                            odd_num.append(k)
                        if type(v) == int and v%2==1:
                            odd_num.append(v)
                elif i%2==1:
                    odd_num.append(i)
            logging.info('all odd numeric values are %s',odd_num)
        except Exception as e:
            logging.exception(e)

    def ineuron_pull(self):
        try:
            value = []
            for i in self.data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j=='ineuron':
                            value.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if k=='ineuron':
                            value.append(k)
                        if v=='ineuron':
                            value.append(v)
                elif i== 'ineuron':
                    value.append(i)
            logging.info('pulling value is %s',value)
        except Exception as e:
            logging.exception(e)


    def num_occur(self):
        try:
            occur=[]
            for i in self.data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        occur.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        occur.append(k)
                        occur.append(v)
                else:
                    occur.append(i)
            for f in occur:
                c=occur.count(f)
                logging.info('%s occurs %s time in data',f,c)
        except Exception as e:
            logging.exception(e)
    def key_num(self):
        '''try to find the out number of keys in dict element'''
        try:
            num=0
            for i in self.data:
                if type(i)==dict:
                    num=num+len(i)
            logging.info(num)
        except Exception as e:
            logging.exception(e)

    def multiplication(self):
        '''try to find out multiplication of each data set individually'''
        try:
            for i in self.data:
                m=1
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            m = m * j
                    logging.info('%s multiplication is %s',type(i), m)
                elif type(i) == dict:
                    for k in i.items():
                        for n in k:
                            if type(n) == int:
                                m = m * n
                    logging.info('%s multiplication is %s',type(i), m)
        except Exception as e:
            logging.exception(e)










