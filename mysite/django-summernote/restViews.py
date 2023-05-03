Rest API - архитектурный стиль взаимодействия компонентов распределенного приложения в сети. Иными словами - это набор правил того, как программисту организовать
написание кода серверного приложения, чтобы все системы легко обменивались данными и приложение можно было масштабировать

Отличительной особенностью сервисов REST является то, что они позволяют наилучшим образом использовать протокол HTTP. Теперь давайте кратко рассмотрим HTTP.

Когда вы вводите в браузере URL-адрес, например www.google.com, на сервер отправляется запрос на веб-сайт, идентифицированный URL-адресом.
Затем этот сервер формирует и выдает ответ. Важным является формат этих запросов и ответов. Эти форматы определяются протоколом HTTP — Hyper Text Transfer Protocol.
Когда вы набираете URL в браузере, он отправляет запрос GET на указанный сервер. Затем сервер отвечает HTTP-ответом, который содержит данные в формате HTML — Hyper Text Markup Language.
Затем браузер получает этот HTML-код и отображает его на экране.
Допустим, вы заполняете форму, присутствующую на веб-странице, со списком элементов. В таком случае, когда вы нажимаете кнопку «Submit» (Отправить), HTTP-запрос POST отправляется на сервер.

Компоненты HTTP

HTTP определяет следующую структуру запроса:

строка запроса (request line) — определяет тип сообщения
заголовки запроса (header fields) — характеризуют тело сообщения, параметры передачи и прочие сведения
тело сообщения (body) — необязательное

HTTP определяет следующую структуру ответного сообщения (response):

строка состояния (status line), включающая код состояния и сообщение о причине
поля заголовка ответа (header fields)
дополнительное тело сообщения (body)

Методы HTTP-запроса

Метод, используемый в HTTP-запросе, указывает, какое действие вы хотите выполнить с этим запросом. Важные примеры:

GET: получить подробную информацию о ресурсе
POST: создать новый ресурс
PUT: обновить существующий ресурс
DELETE: Удалить ресурс

Код статуса ответа HTTP

Код состояния всегда присутствует в ответе HTTP. Типичные примеры:

200 — успех
404 — cтраница не найдена

Фреймворк REST предоставляет APIViewкласс, который является подклассом класса Django View.

APIViewКлассы отличаются от обычных Viewклассов следующими способами:

Запросы, передаваемые методам обработчика, будут экземплярами фреймворка REST , а не экземплярами RequestDjango .HttpRequest
Методы обработчика могут возвращать REST framework Response, а не Django HttpResponse. Представление будет управлять согласованием содержимого и установкой правильного средства визуализации в ответе.
Любые APIExceptionисключения будут перехвачены и преобразованы в соответствующие ответы.
Входящие запросы будут аутентифицированы, и перед отправкой запроса методу обработчика будут выполняться соответствующие проверки разрешений и/или ограничений.


Использование APIViewкласса почти такое же, как использование обычного Viewкласса, как обычно, входящий запрос направляется соответствующему методу обработчика,
такому как .get() или .post(). Кроме того, в классе может быть установлен ряд атрибутов, управляющих различными аспектами политики API.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

https://www.django-rest-framework.org/api-guide/views/
class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


https://www.cdrf.co

Атрибуты политики API
Следующие атрибуты управляют подключаемыми аспектами представлений API.

.renderer_classes
.parser_classes
.authentication_classes
.throttle_classes
.permission_classes
.content_negotiation_class
Методы реализации политики API
Следующие методы используются инфраструктурой REST для создания экземпляров различных подключаемых политик API. Обычно вам не нужно переопределять эти методы.

.get_renderers(self)
.get_parsers(self)
.get_authenticators(self)
.get_throttles(self)
.get_permissions(self)
.get_content_negotiator(self)
.get_exception_handler(self)
Методы реализации политики API
Следующие методы вызываются перед отправкой в ​​метод обработчика.

.check_permissions(самостоятельно, запрос)
.check_throttles(сам, запрос)
.perform_content_negotiation(я, запрос, сила=ложь)
Способы отправки
Следующие методы вызываются непосредственно методом представления .dispatch(). Они выполняют любые действия , которые должны произойти до или после вызова методов обработчика, таких как .get(), .post(), и .put()patch().delete()

.initial(я, запрос, *args, **kwargs)
Выполняет любые действия, которые должны произойти до вызова метода обработчика. Этот метод используется для обеспечения разрешений и регулирования, а также для согласования содержимого.

Обычно вам не нужно переопределять этот метод.

.handle_exception (я, отл.)
Любое исключение, созданное методом обработчика, будет передано этому методу, который либо возвращает экземпляр Response, либо повторно вызывает исключение.

Реализация по умолчанию обрабатывает любой подкласс rest_framework.exceptions.APIException, а также Django Http404и PermissionDeniedисключения и возвращает соответствующий ответ об ошибке.

Если вам нужно настроить ответы на ошибки, которые возвращает ваш API, вы должны подклассировать этот метод.

.initialize_request(я, запрос, *args, **kwargs)
Гарантирует, что объект запроса, передаваемый методу обработчика, является экземпляром Request, а не обычным Django HttpRequest.

Обычно вам не нужно переопределять этот метод.

.finalize_response(я, запрос, ответ, *args, **kwargs)
Гарантирует, что любой Responseобъект, возвращенный из метода обработчика, будет отображаться в правильном типе содержимого, как определено согласованием содержимого.

Обычно вам не нужно переопределять этот метод.

Представления на основе функций
Говорить [что представления на основе классов] всегда являются лучшим решением — ошибка.

— Ник Коглан

Платформа REST также позволяет вам работать с обычными представлениями на основе функций. Он предоставляет набор простых декораторов, которые обертывают ваши представления на основе функций, чтобы гарантировать, что они получают экземпляр Request(а не обычный Django HttpRequest), и позволяют им возвращать Response(вместо Django HttpResponse) и позволяют настроить способ обработки запроса. .

@api_view()
Подпись: @api_view(http_method_names=['GET'])

Ядром этой функциональности является api_viewдекоратор, который принимает список HTTP-методов, на которые должно реагировать ваше представление. Например, вот как вы могли бы написать очень простое представление, которое просто вручную возвращает некоторые данные:

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
Это представление будет использовать рендереры, парсеры, классы аутентификации и т. д. по умолчанию, указанные в настройках .

По умолчанию GETбудут приняты только методы. Другие методы дадут ответ «Метод 405 не разрешен». Чтобы изменить это поведение, укажите, какие методы позволяет представление, например:

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
Декораторы политик API
Чтобы переопределить настройки по умолчанию, платформа REST предоставляет набор дополнительных декораторов, которые можно добавить в ваши представления. Они должны идти после (ниже) @api_viewдекоратора. Например, чтобы создать представление, которое использует дроссель , чтобы убедиться, что он может быть вызван только один раз в день конкретным пользователем, используйте декоратор @throttle_classes, передав список классов дросселя:

from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle

class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})
Эти декораторы соответствуют атрибутам, установленным для APIViewподклассов, описанных выше.

Доступные декораторы:

@renderer_classes(...)
@parser_classes(...)
@authentication_classes(...)
@throttle_classes(...)
@permission_classes(...)
Каждый из этих декораторов принимает один аргумент, который должен быть списком или кортежем классов.

Просмотр декоратора схемы
Чтобы переопределить генерацию схемы по умолчанию для представлений на основе функций, вы можете использовать @schemaдекоратор. Это должно идти после (ниже) @api_view декоратора. Например:

from rest_framework.decorators import api_view, schema
from rest_framework.schemas import AutoSchema

class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        # override view introspection here...

@api_view(['GET'])
@schema(CustomAutoSchema())
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})
Этот декоратор принимает один AutoSchemaэкземпляр, AutoSchemaэкземпляр подкласса или ManualSchemaэкземпляр, как описано в документации по схемам . Вы можете пройти None, чтобы исключить представление из генерации схемы.

@api_view(['GET'])
@schema(None)
def view(request):
    return Response({"message": "Will not appear in schema!"})