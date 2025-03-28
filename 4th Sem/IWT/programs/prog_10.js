try {
  // Create a regular expression that matches any string that starts with "John" and ends with "Smith"
  // The regular expression should also allow for any number of upper or lower case letters in between
  const re = new RegExp("^John.*Smith$", "i");

  // Get the input value from the user
  const input = "John Smith";

  // Test the input value against the regular expression
  if (re.test(input)) {
    console.log("The input matches the pattern!");
  } else {
    console.log("The input does not match the pattern.");
  }
} catch (err) {
  // If there is an error, log it to the console
  console.log("An error occurred: " + err);
}

