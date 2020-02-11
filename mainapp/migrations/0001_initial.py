# Generated by Django 2.2 on 2020-02-11 06:36

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mainapp.models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attestat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название аттестата(сертификата)')),
                ('image', models.ImageField(upload_to='upload/', verbose_name='Скан аттестата')),
                ('number', models.SmallIntegerField(verbose_name='Порядок сортировки')),
            ],
            options={
                'verbose_name': 'Аттестат соответствия',
                'verbose_name_plural': 'Аттестаты соответствия',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.CreateModel(
            name='CenterPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название фотографии')),
                ('image', models.ImageField(upload_to='upload/', verbose_name='Файл')),
                ('number', models.SmallIntegerField(blank=True, verbose_name='Порядок сортировки')),
            ],
            options={
                'verbose_name': 'Фотография центра',
                'verbose_name_plural': 'Фотографии центра',
            },
        ),
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название вставки')),
                ('code', models.CharField(default='КОД_ВСТАВКИ', max_length=64, verbose_name='Уникальный код вставки')),
                ('html', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Форматирование вставки')),
            ],
            options={
                'verbose_name': 'Вставка',
                'verbose_name_plural': 'Вставки',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название компонента')),
                ('code', models.CharField(max_length=60, verbose_name='Шифр компонента (латиницей)')),
                ('component_type', models.CharField(choices=[('attestats', 'Аттестаты соответствия'), ('top_addr_line', 'Верхняя линия с адресом'), ('main_menu', 'Главное меню сайта'), ('secondary_menu', 'Второстепенное меню'), ('main_banner', 'Главный баннер'), ('inner_head', 'Хедер для внутренних страниц'), ('helper_block', 'Вспомогательный заполнятель пустоты'), ('main_page_content', 'Контент главной страницы'), ('pict_gallery', 'Галерея фотографий'), ('text_block', 'Текстовы блок'), ('contact_block', 'Блок с контактами'), ('advertising_block', 'Блок с рекламой'), ('partners_block', 'Блок с партнерами'), ('footer', 'Футер')], default='не определено', max_length=30, verbose_name='Тип компонента(назначение)')),
                ('html', models.FileField(blank=True, default=None, null=True, upload_to='components/', verbose_name='Файл разметки компонента')),
                ('css', models.FileField(blank=True, default=None, null=True, upload_to='components/', verbose_name='Файл стилей компонента')),
                ('js', models.FileField(blank=True, default=None, null=True, upload_to='components/', verbose_name='Файл скриптов')),
                ('html_path', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Путь к файлу разметки')),
                ('relative_html_path', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Относительный путь к файлу разметки')),
                ('scss_path', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Путь к файлу стилей')),
                ('relative_scss_path', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Относительный путь к файлу стилей')),
                ('js_path', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Путь к файлу скрипта')),
                ('relative_js_path', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Относительный путь к файлу скрипта')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовать компонет')),
                ('main_page', models.BooleanField(default=False, verbose_name='Компонент главной страницы')),
                ('number', models.SmallIntegerField(default=500, verbose_name='Порядок вывода на сайт')),
            ],
            options={
                'verbose_name': 'Компонент сайта',
                'verbose_name_plural': 'Компоненты сайта',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название контакта')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('email', models.EmailField(max_length=64, verbose_name='Адрес электронной почты')),
                ('phone', models.CharField(max_length=64, verbose_name='Телефон')),
                ('number', models.SmallIntegerField(default=0, verbose_name='Порядок вывода на сайт')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название')),
                ('document', models.FileField(upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc', 'jpg', 'jpeg'], message='Неправильный тип файла, используйте                                        PDF, DOCX, DOC, JPG, JPEG')], verbose_name='Документ')),
                ('url_code', models.CharField(blank=True, default='НЕ УКАЗАН', max_length=30, verbose_name='Код ссылки')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Загружен')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('publish_on_main_page', models.BooleanField(default=False, verbose_name='Опубиковать на главной')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название категории')),
                ('number', models.SmallIntegerField(blank=True, default=None, null=True, verbose_name='Порядок сортировки')),
            ],
            options={
                'verbose_name': 'Категория документа',
                'verbose_name_plural': 'Категории документов',
            },
        ),
        migrations.CreateModel(
            name='Font',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Название шрифта')),
                ('font_url', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Ссылка на шрифт')),
            ],
            options={
                'verbose_name': 'Шрифт',
                'verbose_name_plural': 'Шрифты',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_code', models.CharField(max_length=30, verbose_name='Код ссылки')),
                ('title', models.CharField(max_length=60, verbose_name='Заголовок ссылки')),
                ('url', models.CharField(default='НЕТ', max_length=200, verbose_name='Адрес ссылки')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='Заголовок')),
                ('typeof', models.CharField(blank=True, max_length=64, verbose_name='Тип сообщения')),
                ('params', models.CharField(blank=True, max_length=512, verbose_name='Параметры сообщения')),
                ('sender_email', models.EmailField(blank=True, max_length=64, verbose_name='Адрес электронной почты')),
                ('sender_phone', models.CharField(blank=True, max_length=64, verbose_name='Телефон')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата получения')),
                ('status', models.IntegerField(choices=[(0, 'new'), (1, 'registered'), (2, 'added_to_sending_queue'), (3, 'notify_sent')], default=0, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='OrderService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя контакта')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон контакта')),
                ('compound', models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='Состав заявки')),
                ('ready', models.BooleanField(blank=True, default=False, null=True, verbose_name='Вопрос решен')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название партнера')),
                ('logo', models.ImageField(upload_to='upload/', verbose_name='Логотип партнера')),
                ('number', models.SmallIntegerField(verbose_name='Порядок вывода на сайт')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('url_code', models.CharField(blank=True, default='НЕ УКАЗАН', max_length=30, verbose_name='Код ссылки')),
                ('short_description', models.CharField(blank=True, max_length=200, verbose_name='Краткое описание')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('publish_on_main_page', models.NullBooleanField(default=False, verbose_name='Опубликовать на главной')),
                ('publish_on_news_page', models.BooleanField(default=False, verbose_name='Опубликовать в ленте новостей')),
                ('publish_in_basement', models.BooleanField(default=False, verbose_name='Опубликовать в подвале на главной')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Страницы',
                'ordering': ['created_date'],
                'get_latest_by': ['created_date'],
                'verbose_name': 'Страница',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_logotype', models.ImageField(blank=True, default=None, null=True, upload_to='upload/', verbose_name='Логотип организации')),
                ('org_footer_logotype', models.ImageField(blank=True, default=None, null=True, upload_to='upload/', verbose_name='Логотип для футера (необязательно)')),
                ('org_short_name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Краткое название организации')),
                ('org_full_name', models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='Полное название организации')),
                ('org_intro', models.TextField(blank=True, default=None, null=True, verbose_name='Текст для главной страницы')),
                ('org_history', models.TextField(blank=True, default=None, null=True, verbose_name='История организаици')),
                ('org_main_phone', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Главный телефон организации (используется в хедере)')),
                ('org_main_phone_text', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Подпись под телефоном в хедере, например "Многоканальный"')),
                ('org_secondary_phone', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Второй телефон организации (используется в хедере)')),
                ('org_secondary_phone_text', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Подпись под вторым телефоном в хедере, например "Бухгалтерия"')),
                ('org_phones', models.TextField(blank=True, default=None, null=True, verbose_name='Телефоны')),
                ('org_email', models.TextField(blank=True, default=None, null=True, verbose_name='Адрес электронной почты')),
                ('org_order_email', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Адреса для подключения формы заявки')),
                ('org_header_emails', models.TextField(blank=True, default=None, null=True, verbose_name='Адреса электронной почты (для хедера)')),
                ('org_header_phones', models.TextField(blank=True, default=None, null=True, verbose_name='Телефоны (для хедера)')),
                ('org_address', models.TextField(blank=True, default=None, null=True, verbose_name='Адрес местоположения организации')),
                ('org_address_map_link', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Ссылка на карту')),
                ('org_work_time', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Время работы организации')),
                ('org_csp_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='шифр ЦСП (необязательно)')),
                ('org_csp_reestr_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр ЦСП')),
                ('org_acsp_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='шифр АЦСП (необязательно)')),
                ('org_acsp_reestr_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр АЦСП')),
                ('org_acsm_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='шифр АЦСМ (необязательно)')),
                ('org_acsm_reestr_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр АЦСМ')),
                ('org_acso_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='шифр АЦСО (необязательно)')),
                ('org_acso_reestr_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр АЦСО')),
                ('org_acst_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='шифр АЦСТ (необязательно)')),
                ('org_acst_reestr_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр АЦСТ')),
                ('org_cok_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='шифр ЦОК (необязательно)')),
                ('org_cok_reestr_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр ЦОК')),
                ('add_ap_list', models.BooleanField(default=False, verbose_name='Добавить ссылку на список пунктов')),
                ('add_schedule', models.BooleanField(default=False, verbose_name='Добавить ссылку на график аттестации')),
                ('number', models.SmallIntegerField(blank=True, null=True, verbose_name='Порядок сортировки')),
            ],
            options={
                'verbose_name': 'Профиль организации',
                'verbose_name_plural': 'Профили организации',
            },
        ),
        migrations.CreateModel(
            name='Profstandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название профстандарта')),
                ('info', models.CharField(max_length=300, verbose_name='Информация о стандарте(код)')),
                ('reg_number', models.CharField(max_length=20, verbose_name='Регистрационный номер')),
                ('mintrud_prikaz', models.CharField(max_length=100, verbose_name='Приказ минтруда')),
                ('document', models.FileField(upload_to='upload/', verbose_name='Файл')),
                ('number', models.SmallIntegerField(verbose_name='Порядок сортировки')),
            ],
            options={
                'verbose_name': 'Профстандарт',
                'verbose_name_plural': 'Профстандарты',
            },
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='Название')),
                ('org', models.CharField(blank=True, max_length=120, verbose_name='Организация')),
                ('typeof', models.CharField(blank=True, max_length=64, verbose_name='Тип')),
                ('params', models.CharField(blank=True, max_length=999, verbose_name='Параметры')),
                ('created_date', models.DateField(blank=True, verbose_name='Дата получения')),
                ('status', models.IntegerField(choices=[(0, 'new'), (1, 'published')], default=0, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Запись реестра',
                'verbose_name_plural': 'Записи реестра',
            },
        ),
        migrations.CreateModel(
            name='SidePanel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Боковая панель',
                'verbose_name_plural': 'Боковые панели',
            },
        ),
        migrations.CreateModel(
            name='SlideBackgrounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Слайдер_2020-02-11 06:36:17.031146+00:00', max_length=50, verbose_name='Название')),
                ('image', stdimage.models.StdImageField(upload_to='backgrounds/', verbose_name='Картинка для фона баннера')),
                ('activated', models.NullBooleanField(default=False, verbose_name='Активировать')),
            ],
            options={
                'verbose_name': 'Картинка для баннера',
                'verbose_name_plural': 'Картинки для баннера',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='uploads/', verbose_name='Фотография')),
                ('name', models.CharField(max_length=120, verbose_name='ФИО')),
                ('job', models.CharField(max_length=120, verbose_name='Должность')),
                ('experience', models.CharField(blank=True, max_length=500, verbose_name='Опыт работы')),
                ('priority', models.SmallIntegerField(default=0, verbose_name='Приоритет')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Конфигурация 1', max_length=30, verbose_name='Название конфигурации')),
                ('site_type', models.CharField(blank=True, choices=[('1', 'site_type1'), ('2', 'site_type2'), ('3', 'site_type3')], default=None, max_length=1, verbose_name='Тип сайта')),
                ('color_set_path', models.CharField(blank=True, default='assets/scss/_variables.scss', max_length=200, null=True, verbose_name='Путь к файлу с переменными SCSS')),
                ('current_color_set', models.CharField(default='#151A18, #E3C4D2, #D6ABBF, #D2E0FF, #968EAF', max_length=50, verbose_name='Текущие цвета')),
                ('current_component_set', models.CharField(blank=True, default='main-menu-v1 main-page-slider-v1 main-page-slider-v3 main-page-content-v1', max_length=300, null=True, verbose_name='Текущий набор компонентов')),
                ('activated', models.BooleanField(default=False, verbose_name='Активировать')),
                ('font', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Font')),
            ],
            options={
                'verbose_name': 'Конфигурация сайта',
                'verbose_name_plural': 'Конфигурации сайта',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='\n            При добавлении услуги в этот раздел автоматически\n            будет создан пункт меню в разделе "Услуги", в котором они\n            сортируются в соответствии с порядком сортировки\n        ', max_length=64, verbose_name='Название услуги')),
                ('short_description', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Краткое описание услуги')),
                ('html', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание услуги')),
                ('number', models.SmallIntegerField(blank=True, default=None, null=True, verbose_name='Порядок сортировки')),
                ('bg_photo', models.ImageField(blank=True, default=None, null=True, upload_to='upload/', verbose_name='Картинка для главной')),
                ('disable_order_button', models.BooleanField(default=False, verbose_name='Отключить кнопку подачи заявки')),
                ('documents', models.ManyToManyField(blank=True, to='mainapp.Document')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Service')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='upload/', verbose_name='изображение')),
                ('title', models.CharField(blank=True, default=mainapp.models.get_image_filename, max_length=64, verbose_name='название')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='Позиция')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='mainapp.Post', verbose_name='новость')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='PostParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=100, verbose_name='Параметр (json)')),
                ('number', models.SmallIntegerField(verbose_name='Порядок вывода')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='side_panel',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.SidePanel', verbose_name='Боковая панель'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='mainapp.Tag', verbose_name='Тэги'),
        ),
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.DocumentCategory'),
        ),
        migrations.AddField(
            model_name='document',
            name='post',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Post', verbose_name='Страница'),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(blank=True, to='mainapp.Tag', verbose_name='Тэги'),
        ),
        migrations.CreateModel(
            name='ComponentParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.CharField(max_length=500, verbose_name='Параметры')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Component')),
            ],
            options={
                'verbose_name': 'Параметр компонента',
                'verbose_name_plural': 'Параметры компонентов',
            },
        ),
        migrations.AddField(
            model_name='component',
            name='configuration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.SiteConfiguration'),
        ),
        migrations.CreateModel(
            name='ColorScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Цветовая схема', max_length=50, verbose_name='Название')),
                ('colors', models.CharField(max_length=100, verbose_name='Цвета (через запятую, HEX)')),
                ('configuration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.SiteConfiguration')),
            ],
            options={
                'verbose_name': 'Цветовая схема',
                'verbose_name_plural': 'Цветовые схемы',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('url_code', models.CharField(blank=True, default='НЕ УКАЗАН', max_length=30, verbose_name='Код ссылки')),
                ('short_description', models.CharField(blank=True, max_length=200, verbose_name='Краткое описание')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('publish_on_main_page', models.BooleanField(default=False, verbose_name='Опубликовать на главной')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('tags', models.ManyToManyField(blank=True, to='mainapp.Tag', verbose_name='Тэги')),
            ],
            options={
                'verbose_name_plural': 'Статьи',
                'ordering': ['created_date'],
                'get_latest_by': ['created_date'],
                'verbose_name': 'Статья',
            },
        ),
    ]
