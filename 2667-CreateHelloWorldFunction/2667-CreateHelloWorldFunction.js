// Last updated: 9/12/2026, 10:19:59 AM
function createHelloWorld() {
    return function(...args) {
        return "Hello World";
    }
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */