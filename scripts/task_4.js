function F1() {
    return new Promise((resolve) => {
        setTimeout(() => resolve("Result1"), 2000);
    });
}

function F2() {
    return new Promise((resolve) => {
        setTimeout(() => resolve("Result2"), 1000);
    });
}

// Суммарный результат обеих функций
Promise.all([F1(), F2()]).then(results => {
    console.log(results.join('')); // "Result1Result2"
});