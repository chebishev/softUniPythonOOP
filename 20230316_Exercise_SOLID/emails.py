from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class XMLContent(IContent):
    def format(self):
        return '\n'.join(['<XML>', self.text, '</XML>'])


class JSONContent(IContent):
    def format(self):
        return '\n'.join(['<JSON>', self.text, '</JSON>'])


class HTMLContent(IContent):
    def format(self):
        return '\n'.join(['<HTML>', self.text, '</HTML>'])


class Protocol:

    def message(self, name):
        return ''.join(["I'm ", name])


class IMProtocol(Protocol):
    pass


class OutlookProtocol(Protocol):
    pass


class IMAPProtocol(Protocol):
    pass


class POP3Protocol(Protocol):
    pass


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = self.protocol.message(sender)

    def set_receiver(self, receiver):
        self.__receiver = self.protocol.message(receiver)

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


im = IMProtocol()
# other protocols for testing:
outlook = OutlookProtocol()
imap = IMAPProtocol()
pop3 = POP3Protocol()

im_email = Email(im)
# other emails for testing:
outlook_email = Email(outlook)
imap_email = Email(imap)
pop3_email = Email(pop3)

im_email.set_sender('qmal')
im_email.set_receiver('james')

my_content = MyContent('Hello, there!')
# other contents for testing:
xml_content = XMLContent('<xml>Hello, there!</xml>')
json_content = JSONContent('{"Hello": "there!"}')
html_content = HTMLContent('<html>Hello, there!</html>')

im_email.set_content(my_content)

print(im_email)
