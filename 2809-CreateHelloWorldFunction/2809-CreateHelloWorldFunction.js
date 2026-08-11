// Last updated: 8/11/2026, 4:03:19 PM
function createHelloWorld() {
    return function(...args) {
        return "Hello World";
    }
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */