from py_hcl.firrtl_ir.expr.literal import SIntLiteral, UIntLiteral
from py_hcl.firrtl_ir.type import UnknownType
from py_hcl.firrtl_ir.type_checker import check, LiteralTypeChecker
from py_hcl.firrtl_ir.type.width import Width
from ..utils import serialize_equal


def test_uint_literal():
    ui = UIntLiteral(10, Width(4))
    assert LiteralTypeChecker.check(ui)
    assert check(ui)
    serialize_equal(ui, 'UInt<4>("a")')

    ui = UIntLiteral(-10, Width(5))
    assert LiteralTypeChecker.check(ui)
    assert check(ui)
    serialize_equal(ui, 'UInt<5>("-a")')

    ui = UIntLiteral(1023, Width(10))
    assert LiteralTypeChecker.check(ui)
    assert check(ui)
    serialize_equal(ui, 'UInt<10>("3ff")')

    ui = UIntLiteral(-1023, Width(11))
    assert LiteralTypeChecker.check(ui)
    assert check(ui)
    serialize_equal(ui, 'UInt<11>("-3ff")')

    ui = UIntLiteral(10, Width(3))
    assert not LiteralTypeChecker.check(ui)
    assert not check(ui)

    ui = UIntLiteral(-10, Width(4))
    assert not LiteralTypeChecker.check(ui)
    assert not check(ui)

    ui = UIntLiteral(10, Width(3))
    ui.tpe = UnknownType()
    assert not LiteralTypeChecker.check(ui)
    assert not check(ui)


def test_sint_literal():
    si = SIntLiteral(10, Width(5))
    assert LiteralTypeChecker.check(si)
    assert check(si)
    serialize_equal(si, 'SInt<5>("a")')

    si = SIntLiteral(-10, Width(5))
    assert LiteralTypeChecker.check(si)
    assert check(si)
    serialize_equal(si, 'SInt<5>("-a")')

    si = SIntLiteral(1023, Width(11))
    assert LiteralTypeChecker.check(si)
    assert check(si)
    serialize_equal(si, 'SInt<11>("3ff")')

    si = SIntLiteral(-1023, Width(11))
    assert LiteralTypeChecker.check(si)
    assert check(si)
    serialize_equal(si, 'SInt<11>("-3ff")')

    si = SIntLiteral(10, Width(4))
    assert not LiteralTypeChecker.check(si)
    assert not check(si)

    si = SIntLiteral(-10, Width(4))
    assert not LiteralTypeChecker.check(si)
    assert not check(si)

    si = SIntLiteral(10, Width(5))
    si.tpe = UnknownType()
    assert not LiteralTypeChecker.check(si)
    assert not check(si)


def test_checker():
    try:
        LiteralTypeChecker.check(123)
    except NotImplementedError:
        assert True
