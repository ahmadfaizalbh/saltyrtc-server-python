import enum

from .exception import *

__all__ = (
    'KEY_LENGTH',
    'NONCE_LENGTH',
    'NONCE_FORMATTER',
    'COOKIE_LENGTH',
    'HASH_LENGTH',
    'RELAY_TIMEOUT',
    'KEEP_ALIVE_TIMEOUT',
    'KEEP_ALIVE_INTERVAL',
    'SubProtocol',
    'CloseCode',
    'AddressType',
    'MessageType',
    'validate_public_key',
    'validate_cookie',
    'validate_initiator_connected',
    'validate_responder_id',
    'validate_responder_ids',
    'validate_hash',
)


KEY_LENGTH = 32
NONCE_LENGTH = 24
NONCE_FORMATTER = '!16s2B6s'
COOKIE_LENGTH = 16
HASH_LENGTH = 32
RELAY_TIMEOUT = 30.0  # TODO: Sane?
KEEP_ALIVE_TIMEOUT = 30.0  # TODO: Sane?
KEEP_ALIVE_INTERVAL = 60.0  # TODO: Sane?


@enum.unique
class SubProtocol(enum.Enum):
    saltyrtc_v1_0 = 'saltyrtc-1.0'


@enum.unique
class CloseCode(enum.IntEnum):
    going_away = 1001
    sub_protocol_error = 1002
    path_full_error = 3000
    protocol_error = 3001
    internal_error = 3002
    data_channel_handover = 3003
    drop_by_initiator = 3004


@enum.unique
class AddressType(enum.IntEnum):
    server = 0x00
    initiator = 0x01
    responder = 0xff

    @classmethod
    def from_address(cls, address):
        if address > 0x01:
            return cls.responder
        else:
            return cls(address)


@enum.unique
class MessageType(enum.Enum):
    """left out client-to-client message types"""
    server_hello = 'server-hello'
    client_hello = 'client-hello'
    client_auth = 'client-auth'
    server_auth = 'server-auth'
    new_responder = 'new-responder'
    new_initiator = 'new-initiator'
    drop_responder = 'drop-responder'
    send_error = 'send-error'


def validate_public_key(key):
    if not isinstance(key, bytes) or len(key) != KEY_LENGTH:
        raise MessageError('Invalid key')


def validate_cookie(cookie):
    if not isinstance(cookie, bytes):
        raise MessageError('Invalid cookie: Must be `bytes` instance')
    if len(cookie) != COOKIE_LENGTH:
        raise MessageError('Invalid cookie: Invalid length (%d != %d)'
                % (len(cookie), COOKIE_LENGTH))


def validate_initiator_connected(initiator_connected):
    if not isinstance(initiator_connected, bool):
        raise MessageError("Invalid value for field 'initiator_connected'")


def validate_responder_id(responder):
    if not isinstance(responder, int) or not 0x01 < responder <= 0xff:
        raise MessageError('Invalid responder in responder list')


def validate_responder_ids(responders):
    try:
        iterator = iter(responders)
    except TypeError as exc:
        raise MessageError('Responder list is not iterable') from exc
    for responder in iterator:
        validate_responder_id(responder)


def validate_hash(hash_):
    if not isinstance(hash_, bytes) or len(hash_) != HASH_LENGTH:
        raise MessageError('Invalid hash')
