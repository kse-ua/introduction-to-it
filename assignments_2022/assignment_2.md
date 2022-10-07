###### Практична робота №2
## Про житло та кредити

### Мета роботи:
Попрактикуватись у використанні базових концептів мови Python: змінні, умови, цикли, типи даних, робота з введенням та виведенням (i\o, input\ouput).

## Завдання

#### Перший етап
Після закінчення KSE ви знайшли собі гарну роботу та вирішили пригледіти собі квартиру у Києві. Нерухомість у столість дорога, тому доведеться брати кредит. Для того щоб взяти кредит, потрібно зробити стартовий внесок, що також є немаленькою сумою. Оскільки ви закінчили KSE, то ви вирішуєте інвестувати частину грошей для того щоб назбирати на стартовий внесок. Наприклад:

> Квартира коштує $100000. Стартовий внесок - 30%, вам потрібно зібрати $30000. Відкладаючи по $500 щомісяця, це можна зробити за 60 місяців, або 5 років. Якщо ж відкладати не в сейф, а інвестувати під 10% річних, то суму можна зібрати на рік раніше - за 48 місяців.
1. Спитайте у користувача його заробітну плату та який відсоток грошей він готовий відкладати;
2. Спитайте вартість нерухомості та необхідний відсоток стартового внеску;
3. Спитайте, яка дохіднісь інвестиций у рік у відсотках. Вважайте, що ви отримуєте дохід від інвестицій щомісяця;
4. Порахуйте та виведіть, скільки років та місяців потрібно буде відкладати, перш ніж на вашому рахунку буде сума, достатня для стартового внеску. При виведенні вказуйте кількість років, наприклад, `1 рік 5 місяців`, а не `17 місяців`

> Ви відкладаєте щомісяця $100 та маєте річну доходність у 4%. Після першого місяця ви ще нічого не відклали, тому і відсотків немає, але ви отримуєте свої перші $100 на рахунок. Після другого ви отримуєте ще $100 із окладу, плюс 100 * 0.04 / 12 = $0.34 відсотків. Після третього місяця ви отримуєте ще $100 з окладу, але відсотки нараховуються на всі ваші збереження, 200.34 * 0.04 / 12 = $0.67 і сумарно ви маєте вже $301


#### Другий етап
Із стартовим внеском розібралися, але лишається ще тіло кредиту, яке треба виплатити разом із відсотками. Наприклад:
> Та ж квартира коштує $100000, відсотки по кредиту - 5% річних. Якщо ви берете кредит на три роки, то маєте сумарно виплатити 100000 * 5% * 3 = $15000. Загальна сума стає $115000, без стартового внеску $85000 або $2360 щомісяця протягом трьох років.
1. Спитайте після виконання програми з попереднього пункту, чи хоче користувач порахувати і тіло кредиту. Якщо не хоче, програма має закінчити виконання.
2. Якщо хоче, спитайте кількість років кредитування та річний відсоток.
3. Порахуйте, скільки потрібно буде виплачувати щомісяця. Якщо ця сума більша за заробітну плату, виведіть окреме повідомлення про те що подібний кредит не можливо взяти за таких умов.

#### Третій етап
Для третього етапу ми підемо далі, скопіюйте створену програму в окремий файл (щоб можна було окремо показати та здати попередні етапи). Вас не влаштовує той факт, що обираючи між довжиною кредитів ви отримуєте або занадто великий місячний платіж (дорого), або занадто малий (багато платити по відсотках, хочеться швидше). Враховуючи ваш дохід, ви хочете визначитися, на скільки місяців потрібно брати кредит, для того щоб щомісяця платити фіксовану, максимально зручну для вас суму.

Модифікуйте програму, так щоб не питати тривалість кредиту, а навпаки - спитати рівень комфортного платежу (у долларах, щомісячно) та порахуйте за цими даними, на скільки місяців треба взяти кредит. 

#### Четвертий етап
Для цього етапу зробіть ще одну копію програми з другого пункту. Ви закінчили університет, тому маєте амбіції на успішну карʼєру і розраховуєте що ваша заробітна плата буде зростати, і відповідно ви зможете більше відкладати. Модифікуйте програму так, щоб вона питала заплановне зростання заробітної плати. Зростання має враховуватись кожні півроку - тобто після 6, 12, 18 і так далі місяців. Під час прорахунку тіла кредиту, враховуйте що на момент коли ви накопичете стартову суму та почнете виплачувати кредит, ваша заробітна плата вже буде вищою

#### Пʼятий, додатковий, етап
**Цей етап є складним та трохи випереджає нашу програму, тому його не обовʼязково виконувати. Але якщо ви його зробите, зможете отримати додаткові 1.5 бали**

Припустимо, ви хочете поставити конкретну ціль - зібрати на стартовий внесок кредиту за 2 роки. Порахуйте та виведіть, який відсоток окладу вам потрібно відкладати, враховуючи регулярне зростання вашого окладу та інвестування.

Для цього завдання, вам варто згадати прилад про пошук картки в бібліотеці з лекції та уважніше почитати про [двійковий пошук](https://en.wikipedia.org/wiki/Bisection_method). Цей метод зможе допомогти вам підібрати число, наближаючись за певну кількість кроків до найкращого відсотка.

## Контрольні питання
- Як ви розумієте поняття рівнів абстракції?
- Що таке тип даних, які ви знаєте?
- Що таке правила Де Моргана?
- Яким чином у Python можна створити цикл?

## Оцінювання

Максимальний бал - 4 (+1.5):
- 1 бал - перший та другий етапи;
- 1 бал - третій та четвертий етапи;
- 1 бал - виконання додаткового завдання на парі;
- 1 бал - відповідь на теоретичні питання при здачі;
- +1.5 додаткових бали за пʼятий етап;


## Матеріали для виконання
1. [Basic data types and operations](https://hyperskill.org/knowledge-map/991?track=6)
2. [Programs with numbers
   ](https://hyperskill.org/learn/step/5872). 
3. [Boolean logic](https://hyperskill.org/knowledge-map/983?track=6)
4. [Control flow statements](https://hyperskill.org/knowledge-map/423?track=6)