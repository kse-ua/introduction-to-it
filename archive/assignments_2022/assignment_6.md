###### Практична робота №6
## Вивчаємо Git

### Мета роботи:
Познайомитись з концептом системи контролю версій, вивчити базові поняття Git та підготуватись до виконання групових завдань, починаючи з практичної №7.

## Завдання

Ця робота складається з двох частин - в першій ви спробуєте попрацювати з гітом у оноайн-грі з рівнями, де ви будете захищені від випадкових помилок та зможете сконцентруватись на головному. Отже,

### Перша частина

Виконайте всі вправи [звідси](https://learngitbranching.js.org/). Зверніть увагу, що там є дві вкладки із завданнями, вам треба виконати завдання з обох. Внизу є кнопка для зміни мови, ви можете проходити гру як англійською, так і українською мовою. Виконуйте завдання уважно, під час здачі роботи вам буде потрібно у класі повторно пройти один із останніх рівнів. 

В цих завданнях відсутні хіба що самі зміни в кожному комміті, і немає конфліктів при зливанні гілок. Ну і ще немає незрозумілих помилок від гіта. Тому,

### Друга частина

Має на меті надолужити цей недолік. Таким чином, ця робота підготує вас  до повноцінного використання git вже із наступної практичної.

Для початку, вам потрібен власний аккаунт на [GitHub](https://github.com/), якщо у вас його ще немає. Ви можете використовувати як особисту, так і університетську пошту (до аккаунту на гітхабі можна прив'язувати декілька поштових скриньок). Обов'язково вкажіть в профілі повне ім'я та прізвище!

Далі, зробіть fork [цього репозиторію](https://github.com/kse-ua/git-playground). В ньому знаходиться невеличка гра на Python, де користувачу потрібно скласти 5 слів із літер слова, яке надає компʼютер. Достатньо натиснути кнопку Fork в правому верхньому куті сторінки. Це створить копію у вашому профілі, яку ви можете змінювати, як заманеться. Будь ласка, не клонуйте сам репозиторій, у вас не вийде зробити push, бо доступ до нього обмежений.

Основна гілка називається master. Саме її вам треба для початку [клонувати](https://git-scm.com/book/uk/v2/Основи-Git-Створення-Git-репозиторія) на свій комп'ютер. Із цим можуть виникнути труднощі, якщо ви хочете використовувати протокол ssh. Рекомендую почати із https: при цьому вам доведеться вводити логін/пароль, проте не треба буде витрачати час і розбиратися з ssh ключами.

Після того, як завантажите репозиторій спробуйте зливати інші гілки в master:

* `no-conflicts-branch` має зливатися без жодних конфліктів, merge або rebase просто створить новий комміт. Це хороший випадок, коли вам не треба нічого виправляти вручну.
* `conflict-branch змінює` ту  саму частину коду, що змінювалась в master, тому git відмовиться робити щось самостійно і запропонує виправити конфлікт власноруч. Вирішіть конфлікт так, щоб в підсумку в конфліктній функції лишилось оформлення повідомлення як в цій гілці, але було видно всі слова що ввів користувач, як в основній.

Можете використовувати як merge, так і rebase, щоб пересвідчитися, що вони працюють так само, як у грі з першої частини. Спробуйте також хоча б один раз розібратися з конфліктом без GUI, за допомогою консолі і звичайного текстового редактора. Ви побачите, як виглядають файли в процесі злиття двох конфліктуючих гілок (приблизно `<<<<<<<HEAD<<<<<<<<<<master ===================>>>>>>your!!!!>>>>>>>><<<<<<<<<theirs!!!!!!!!!<<<<<<======<<<<<<<<`) і в майбутньому будете розуміти, що ці символи значать і звідки вони взялися.

Далі зробіть нову гілку improvements, в цій гілці додайте в програму перевірку того, щоб користувач не міг двічі або більше вводити одне і те саме слово. Також додайте окреме повідомлення якщо гравець програє (окремим коммітом). Піся цього мерджем злийте цю гілку в основний репозиторій.

Ви можете стикнутися з безліччю дивних помилок при роботі з git, це абсолютно нормально. Будь ласка, пишіть повідомлення про помилки в чати, питайте на практичних та office hours і будемо розбиратися разом.

## Матеріали
- [Коротка довідка](/assignments_2022/res/git_gui.md) по роботі з візуальним клієнтом;
- [Офіцйна книжка по Git](https://git-scm.com/book/uk/v2). Вам знадобляться перші 3 розділи
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

Будь-ласка, не починайте робити другу частину завдання, поки ви не пройшли повністю першу. Робота зі справжнім репозиторієм вимагає знань багатьох концепцій, з якими ви можете познайомитсь через гру learn git branching

## Контрольні питання
- Які задачі вирішує Git?
- Опишіть поняття: комміт, репозиторій, гілка (branch), pull\push, fork;
- Для чого потрібні rebase та merge, в чому між ними різниця?
- Що таке HEAD? 
- Що таке origin?

## Оцінювання

Максимальний бал - 5:
- 1 бали - вирішення всіх завдань у learn git branching;
- 1 бал - перевірочне завдання з learn git branching;
- 1 бал - завдання у справжньому репозиторії;
- 1 бал - відповідь на питання при здачі;
- 1 бал - виконання додаткового практичного завдання при здачі.
