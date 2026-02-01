const services = {
    toSit: 500,
    toJump: 1200,
    toLayDown: 300,

    price: function () {
        let total = 0;

        for (let key in this) {
            if (typeof this[key] === "number") {
                total += this[key];
            }
        }

        return total;
    },

    minPrice: function () {
        let min = null;

        for (let key in this) {
            if (typeof this[key] === "number") {
                if (min === null || this[key] < min) {
                    min = this[key];
                }
            }
        }

        return min;
    },

    maxPrice: function () {
        let max = null;

        for (let key in this) {
            if (typeof this[key] === "number") {
                if (max === null || this[key] > max) {
                    max = this[key];
                }
            }
        }

        return max;
    }
};

console.log(services.price());
console.log(services.minPrice());
console.log(services.maxPrice());
console.log('=============================================');

services.toRun = 1600;
console.log('Additional service - plus ' + services.toRun);
console.log('=============================================');

console.log(services.price());
console.log(services.minPrice());
console.log(services.maxPrice());
console.log('=============================================');

services.toShrug = 200;
console.log('Additional service - plus ' + services.toShrug);
console.log('=============================================');

console.log(services.price());
console.log(services.minPrice());
console.log(services.maxPrice());