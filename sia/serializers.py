# Serializers
def serialize_int8_array_item(sia: Sia, n: int) -> Sia:
    return sia.add_int8(n)

def serialize_int16_array_item(sia: Sia, n: int) -> Sia:
    return sia.add_int16(n)

def serialize_int32_array_item(sia: Sia, n: int) -> Sia:
    return sia.add_int32(n)

def serialize_int64_array_item(sia: Sia, n: int) -> Sia:
    return sia.add_int64(n)

def serialize_uint8_array_item(sia: Sia, n: int) -> Sia:
    return sia.add_uint8(n)

def serialize_uint16_array_item(sia: Sia, n: int) -> Sia:
    return sia.add_uint16(n)

def serialize_uint32_array_item(sia: Sia, n: int) -> Sia:
    return sia.add_uint32(n)

def serialize_uint64_array_item(sia: Sia, n: int) -> Sia:
    return sia.add_uint64(n)

def serialize_string8_array_item(sia: Sia, n: str) -> Sia:
    return sia.add_string8(n)

def serialize_string16_array_item(sia: Sia, n: str) -> Sia:
    return sia.add_string16(n)

def serialize_string32_array_item(sia: Sia, n: str) -> Sia:
    return sia.add_string32(n)

def serialize_string64_array_item(sia: Sia, n: str) -> Sia:
    return sia.add_string64(n)

def serialize_byte_array8_array_item(sia: Sia, n: bytes) -> Sia:
    return sia.add_byte_array8(n)

def serialize_byte_array16_array_item(sia: Sia, n: bytes) -> Sia:
    return sia.add_byte_array16(n)

def serialize_byte_array32_array_item(sia: Sia, n: bytes) -> Sia:
    return sia.add_byte_array32(n)

def serialize_byte_array64_array_item(sia: Sia, n: bytes) -> Sia:
    return sia.add_byte_array64(n)

def serialize_bool_array_item(sia: Sia, n: bool) -> Sia:
    return sia.add_bool(n)

# Deserializers
def deserialize_int8_array_item(sia: Sia) -> int:
    return sia.read_int8()

def deserialize_int16_array_item(sia: Sia) -> int:
    return sia.read_int16()

def deserialize_int32_array_item(sia: Sia) -> int:
    return sia.read_int32()

def deserialize_int64_array_item(sia: Sia) -> int:
    return sia.read_int64()

def deserialize_uint8_array_item(sia: Sia) -> int:
    return sia.read_uint8()

def deserialize_uint16_array_item(sia: Sia) -> int:
    return sia.read_uint16()

def deserialize_uint32_array_item(sia: Sia) -> int:
    return sia.read_uint32()

def deserialize_uint64_array_item(sia: Sia) -> int:
    return sia.read_uint64()

def deserialize_string8_array_item(sia: Sia) -> str:
    return sia.read_string8()

def deserialize_string16_array_item(sia: Sia) -> str:
    return sia.read_string16()

def deserialize_string32_array_item(sia: Sia) -> str:
    return sia.read_string32()

def deserialize_string64_array_item(sia: Sia) -> str:
    return sia.read_string64()

def deserialize_byte_array8_array_item(sia: Sia) -> bytes:
    return sia.read_byte_array8()

def deserialize_byte_array16_array_item(sia: Sia) -> bytes:
    return sia.read_byte_array16()

def deserialize_byte_array32_array_item(sia: Sia) -> bytes:
    return sia.read_byte_array32()

def deserialize_byte_array64_array_item(sia: Sia) -> bytes:
    return sia.read_byte_array64()

def deserialize_bool_array_item(sia: Sia) -> bool:
    return sia.read_bool()
