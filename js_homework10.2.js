const meetings = "Meetings. Since 2000, the amount of time that we spend in meetings has increased by an estimated 10% per year. An average meeting lasts 30 to 60 minutes, and we attend up to 10 meetings a week. \n " +
    "A recent study in the USA revealed that workers spend an average of two hours a week in pointless meetings. Two hours per person per week has been estimated at $400 billion per year of lost productivity. \n " +
    "However, meetings are also important for connecting colleagues, sharing ideas and for fostering innovation and creativity. \n " +
    "Some tips to make meetings more productive include having an agenda and sharing it before the meeting. Limit the discussion time, take notes, and define clear action points to be followed afterwards. \n " +
    "Some companies have limited meetings to just one day per week. With this restriction, employees report that many issues are resolved without waiting until the next meeting day."

const pattern = /\b[^aA\s]{6,}\b/g;
const result = meetings.match(pattern);
console.log(result);