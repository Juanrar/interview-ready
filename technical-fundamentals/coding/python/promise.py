"""
Regretfully, at Silver we do sometimes break our promises.
We wanted to express this in code, but Javascript's native Promises are not easy to modify.
We need to implement our own Promises that mimic and extend Javascript's core promises.

Step 1
------
Implement native style promises with the methods then and catch.
You can consult the reference at https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

The executor receives two functions, resolve and reject:

    SilverPromise(lambda resolve, reject: resolve(42))

Notes:
- Promise chaining must be supported
- Then functions carry over resolution values to future calls of the function
- If the promise is already resolved, then() calls its callback right away
- resolve and reject can be called from another thread (the tests use threading.Timer)

Step 2
------
Implement a "break_" method that prevents previous callbacks from being called.
(break is a reserved word in Python.)
"""

import threading
import time
from typing import Any, Callable
from unittest.mock import Mock


class SilverPromise:
    def __init__(self, executor: Callable[[Callable, Callable], None]):
        pass

    def then(self, on_fulfilled: Callable[[Any], Any]) -> "SilverPromise":
        pass

    def catch(self, on_rejected: Callable[[Exception], Any]) -> "SilverPromise":
        pass

    def break_(self) -> None:
        pass


# Tests


def later(seconds: float, fn: Callable[[], None]) -> None:
    threading.Timer(seconds, fn).start()


def test_resolves_and_calls_then():
    fulfillment = []
    promise = SilverPromise(lambda resolve, reject: later(0.1, lambda: resolve("Success")))

    promise.then(lambda result: fulfillment.append(result))

    time.sleep(0.2)
    assert fulfillment == ["Success"]


def test_catches_errors():
    errors = []
    promise = SilverPromise(
        lambda resolve, reject: later(0.1, lambda: reject(Exception("Failure")))
    )

    promise.catch(lambda error: errors.append(error))

    time.sleep(0.2)
    assert len(errors) == 1
    assert str(errors[0]) == "Failure"


def test_chains_then_with_unresolved_promise():
    promise = SilverPromise(lambda resolve, reject: later(0.1, lambda: resolve(0)))
    then0 = Mock(return_value=1)
    then1 = Mock(return_value=2)
    then2 = Mock()

    promise.then(then0).then(then1).then(then2)

    time.sleep(0.2)
    then0.assert_called_with(0)
    then1.assert_called_with(1)
    then2.assert_called_with(2)


def test_chains_then_with_resolved_promise():
    promise = SilverPromise(lambda resolve, reject: resolve(0))
    then0 = Mock(return_value=1)
    then1 = Mock(return_value=2)
    then2 = Mock()

    promise.then(then0).then(then1).then(then2)

    then0.assert_called_with(0)
    then1.assert_called_with(1)
    then2.assert_called_with(2)


def test_breaks_promises():
    calls = []
    promise = SilverPromise(lambda resolve, reject: later(0.1, lambda: resolve("Success")))

    promise.then(lambda result: calls.append("Should never be called"))
    promise.break_()

    time.sleep(0.2)
    assert calls == []
