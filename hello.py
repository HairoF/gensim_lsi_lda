import numpy
from scipy import linalg
from math import sqrt
import nltk


from nltk.stem.snowball import RussianStemmer

stemmer = RussianStemmer()

nltk.download('stopwords')
from nltk.corpus import stopwords

stopw = stopwords.words('russian')


class LSI(object):
    def __init__(self, stopw, ignorechars, docs):
        self.docs = []
        self.wdict = {}
        self.dictionary = []
        self.stopwords = stopw
        if type(ignorechars) == str:
            ignorechars = ignorechars.encode('utf-8')
            self.ignorechars = ignorechars
        for doc in docs:
            self.add_doc(doc)

    def prepare(self):
        self.build()
        self.calc()

    def dic(self, word, add=False):
        if type(word) == str:
            word = word.encode('utf-8')
            word = word.lower().translate(None, self.ignorechars)
            word = word.decode('utf-8')
            word = stemmer.stem(word)
        if word in self.dictionary:
            return self.dictionary.index(word)
        else:
            if add:
                self.dictionary.append(word)
                return len(self.dictionary) - 1
            else:
                return None

    def add_doc(self, doc):
        words = [self.dic(word, True) for word in doc.lower().split()]
        self.docs.append(words)
        for word in words:
            if word in self.stopwords:
                continue
            elif word in self.wdict:
                self.wdict[word].append(len(self.docs) - 1)
            else:
                self.wdict[word] = [len(self.docs) - 1]

    def build(self):
        self.keys = [k for k in self.wdict.keys() if len(self.wdict[k]) > 0]
        self.keys.sort()
        self.A = numpy.zeros([len(self.keys), len(self.docs)])
        for i, k in enumerate(self.keys):
            for d in self.wdict[k]:
                self.A[i, d] += 1

    def calc(self):
        self.U, self.S, self.Vt = linalg.svd(self.A)

    def TFIDF(self):
        wordsPerDoc = sum(self.A, axis=0)
        docsPerWord = sum(numpy.asarray(self.A > 0, 'i'), axis=1)
        rows, cols = self.A.shape
        for i in range(rows):
            for j in range(cols):
                self.A[i, j] = (self.A[i, j] / wordsPerDoc[j]) * numpy.log(float(cols) / docsPerWord[i])

    def dump_src(self):
        self.prepare()
        print('Здесь представлен расчет матрицы ')
        for i, row in enumerate(self.A):
            print(self.dictionary[i], row)

    def print_svd(self):
        self.prepare()
        print('Здесь сингулярные значения')
        print(self.S)
        print('Здесь первые 3 колонки U матрица ')
        for i, row in enumerate(self.U):
            print(self.dictionary[self.keys[i]], row[0:3])
        print('Здесь первые 3 строчки Vt матрица')
        print(-1 * self.Vt[0:3, :])

    def find(self, word):
        self.prepare()
        idx = self.dic(word)
        if not idx:
            print('слово невстерчается')
            return []
        if not idx in self.keys:
            print('слово отброшено как не имеющее значения которое через stopwords')
            return []
        idx = self.keys.index(idx)
        print('word --- ', word, '=', self.dictionary[self.keys[idx]], '.\n')
        # получаем координаты слова
        wx, wy = (-1 * self.U[:, 1:3])[idx]
        print('word {}\t{:0.2f}\t{:0.2f}\t{}\n'.format(idx, wx, wy, word))
        arts = []
        xx, yy = -1 * self.Vt[1:3, :]
        for k, v in enumerate(self.docs):
            ax, ay = xx[k], yy[k]
            dx, dy = float(wx - ax), float(wy - ay)
            arts.append((k, v, ax, ay, sqrt(dx * dx + dy * dy)))
        return sorted(arts, key=lambda a: a[4])


docs = [
    "Верстать сайты в html и CSS Разрабатывать клиентскую часть сайта на React Программировать на языках JavaScript и TypeScript Работать с базами данных с использованием MongoDB Создавать серверную часть на Node.js, Express.js, Nest.js Работать с API сторонних сервисов и проводить Unit-тестирование Новичкам в программировании Начинающим разработчикам Frontend и backend разработчикам",
    "Работать с инструментами разработки Node.js; Использовать библиотеки и фреймворки Node.js: Express.js, Nest.js; Писать на TypeScript и использовать инструменты tsc, tslint/eslint; Подключать и использовать в проекте базы данных (MongoDB); Настраивать обмен данными между клиентом и сервером (WebSocket); Работать с ПО для автоматизации развёртывания и управления приложениями (Docker); Настраивать аутентификацию с помощью Passport.js; Писать unit-тесты; Использовать Google Firebase",
    "Работа с props, управление внутренним состоянием компонента и обработка данных из форм; Владею продвинутыми техниками композиции компонентов и работы с дочерними компонентами; Использую самое современное API: хуки и Context API",
    "Вёрстка сайтов в html и CSS; Работа с frontend-частью проекта на JavaScript; Работа с backend-частью проекта на PHP; Работа с изменениями кода проекта с помощью Git и GitHub; Разработка сайтов с помощью фреймворка Bitrix; Управление сайтами на платформе 1C-Bitrix; Работа с API сторонних сервисов; Работа с новым ядром платформы Bitrix D7",
    "Вёрстка под тач и мобильные устройства; Работа с Flexbox и JavaScript; Способность правильно использовать переменные, числа и строки; Создание прототипа и конструктора объекта; Использование выражений в JavaScript; Применение символов, итераторов и генераторов; Импорт и экспорт модулей; Создание интерактивных веб-страниц; Работа с файлами и медиаресурсами; Применение принципов клиент-серверного взаимодействия; Создание одностраничных веб-приложений (SPA); Навыки использования библиотеки React,  JSX, React router, VirtualDom",
    "Сбор и подготовка данных для анализа; Умение писать сложные запросы на SQL; Импорт и экспорт данных; Понимание архитектуры и структуры БД; Группировка и фильтрация данных из БД; Работа с разными форматами файлов",
    "Построение работы сетей и работы сетевого стека; Создание распределённых информационных систем; Аудит информационных систем в области информационной безопасности; Построение системы информационной безопасности; Понимание типов атак на информационные системы и используемых механизмов ; Анализ инцидентов и разработка мер реагирования; Знание криптографических и некриптографических методов защиты информации, влияния человеческого фактора; Знание нормативно-правовых актов в сфере ИБ Российской Федерации, сфере ответственности государственных структур: ФСТЭК, ФСБ, Министерство Обороны, ЦБ; Владение Kubernetes на продвинутом уровне, разворачивание кластера Kubernetes, работа с конфигурацией и сетевой безопасностью; Знание международного законодательства, отраслевых стандартов: PCI-DSS, OWASP ; Работа с операционными системами ",
]
ignorechars = '`"'':,;!'
word = "html"
lsa = LSI(stopw, ignorechars, docs)
lsa.build()
lsa.dump_src()
lsa.calc()
lsa.print_svd()

for res in lsa.find(word):
    print(res[0], res[4], res[1], docs[res[0]])
