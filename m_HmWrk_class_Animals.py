## Домашняя работа, задача №1 "Ферма дядюшки Джо"    
class Animals():  ## создаём класс животных с собственными именами и методами def *(self) именно методами! так как они буду относится к конкретному объекту
    
    ctr = 0  ## счётчик
    weight_dict = {}  ## словарь весов
    name_dict = {}  ## имён
    sum_wh = 0  ## сумма веса всех животных
    most_heavy = 0  ## тяжеловес

    def __init__(self,typeof,name,weight):  ## конструктор класса
        self.typeof = typeof
        self.name = name
        self.wheit = weight
        type(self).ctr +=1  ## счётчик создания объектов класса
        self.id = type(self).ctr  ## записываем id
        self.weight_dict.setdefault(self.id, self.wheit)  ## добавляем в общий словарь id животного с его весом
        self.name_dict.setdefault(self.id, self.name)  ## добавляем в общий словарь id животного с его именем

    
    voice = {'guss':'Ga_Ga',  ## такой способ = swich-case, мы из словаря по ключу выберем свойство для типа животного
             'cow':'Mu_Mu',
             'sheep':'Be_Be',
             'chiken':'Ko_Ko',
             'duck':'Krya'}

    resours_coll = {'guss':'EGGS',  ## сбор ресурсов
             'cow':'MILK',
             'sheep':'WOOL',
             'chiken':'EGGS',
             'duck':'EGGS'}

    def Get_name(self):
        name = self.name

    def Info(self):  ## получаем словарь __dict__ объекта (инфо)
        print(self.__dict__)

    def Eating(self): 
        print(f'кормёжка', self.typeof)
    
    def Voise(self): ## получаем Voice из словаря voice по ключу self.typeof 
        print(f'{self.typeof} издаёт звук:',self.voice.get(self.typeof))

    def Resoure_Coll(self):  ## тоже самое и для сбора ресурсов
        print(f'{self.typeof} создаёт ресурс:',self.resours_coll.get(self.typeof))

## Создаём объекты класса Животные(Animals)
anim1 = Animals('guss','Gena',12)                            
print('Animal_Info:',anim1.__dict__)                        ##
anim1.Eating()
anim1.Voise()
anim1.Resoure_Coll()
print('\n')

anim2 = Animals('cow','Milka',5150)
print('Animal_Info:',anim2.__dict__)
anim2.Eating()
anim2.Voise()
anim2.Resoure_Coll()
print('\n')

anim3 = Animals('sheep','Vasya',2850)
print('Animal_Info:',anim3.__dict__)
anim3.Eating()
anim3.Voise()
anim3.Resoure_Coll()
print('\n')


print(f'Словарь веса:',Animals.weight_dict)
print(f'Словарь имён:',Animals.name_dict,'\n')


def SumWght_MstHv(wd = Animals.weight_dict,nd = Animals.name_dict):  ## функция нахождения суммарого веса объектов и самого тяжёлого из них
    sum_wght = 0
    most_heavy = 0
    for x in wd:  ## листаем словарь веса
        #print(x)
        #print(self.weight_dict.get(x))
        sum_wght += wd.get(x)  ## получаем из словаря весов значение и суммируем
        if wd.get(x)>most_heavy:  ## находим самого тяжёлого
            most_heavy = wd.get(x)
            id_hw = x             ## записываем id самого тяжёлого
    print(f'{nd.get(id_hw)} весит больше всех:',most_heavy)  ## достаём из словаря имён имя по id
    print('Общий вес животных:',sum_wght)

SumWght_MstHv()
