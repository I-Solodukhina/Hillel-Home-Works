let arr = [
    {
        userName:"Test",
        lastName:"Test",
        email:"test.test@test.com"
    },
    {
        userName:"Dmytro",
        lastName:"Porokhov",
        email:"dmitro.porokhov@yahoo.com>"
        },
    {
        userName:"Andrey",
        lastName:"",
        email:"andrey@mail.ru"
    },
    {
        userName:"Andrii",
        lastName:"Borovyi",
        email:"andrii.b@gmail.com"
    },
    {
        userName:"Mykyta",
        lastName:"Lys",
        email:"lys.mykyta@gmail.com"
    },
    {
        userName:"Tetiana",
        lastName:"Golovko",
        email:"teti.g@yahoo.com"
    },
    {
        userName:"Maryna",
        lastName:"Shmyg",
        email:"shmyg.m.a@yahoo.com"
    },
    {
        userName:"Makar",
        lastName:"Vovk",
        email:"makar.yahoo.com"
    },
];


const emailReg = /^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@(gmail\.com|yahoo\.com)$/;

const correctEmails = [];

for (let i = 0; i < arr.length; i++) {
    if (emailReg.test(arr[i].email)) {
        correctEmails.push(arr[i].email);
    }
}

console.log(correctEmails);