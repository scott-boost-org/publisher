type Person = {
  firstName: string;
  lastName: string;
  dateOfBirth: Date;
  socialInsuranceNumber: number;
  postalCode: string;
};

const greet = (person: Person) => {
  console.log(person)
}
