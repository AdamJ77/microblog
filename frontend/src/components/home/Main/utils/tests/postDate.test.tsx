import { calculateTimeDifference, formatTimeDifference } from "../postDate";

describe("date utils for posts", () => {
  describe("calculateTimeDifference", () => {
    it("correctly calculates datetime difference", () => {
      const oldDate = new Date(2023, 9, 29, 22, 13, 12);
      const newDate = new Date(2023, 10, 12, 17, 2, 21);

      const result = calculateTimeDifference(newDate, oldDate);

      const expectedDays = 13;
      const expectedHours = expectedDays * 24 + 18;
      const expectedMinutes = expectedHours * 60 + 49;
      const expectedSeconds = expectedMinutes * 60 + 9;
      const expectedMilliseconds = expectedSeconds * 1000;

      expect(result).toEqual({
        milliseconds: expectedMilliseconds,
        seconds: expectedSeconds,
        minutes: expectedMinutes,
        hours: expectedHours,
        days: expectedDays,
        weeks: 1,
        months: 0,
        years: 0,
      });
    });

    it("correctly calculates datetime difference when previous year", () => {
      const oldDate = new Date(2022, 11, 29, 22, 13, 12);
      const newDate = new Date(2023, 10, 12, 17, 2, 21);

      const result = calculateTimeDifference(newDate, oldDate);

      const { months, years } = result;

      expect(months).toBe(10);
      expect(years).toBe(0);
    });

    it("correctly calculates datetime difference when more than a year ago", () => {
      const oldDate = new Date(2021, 11, 29, 22, 13, 12);
      const newDate = new Date(2023, 10, 12, 17, 2, 21);

      const result = calculateTimeDifference(newDate, oldDate);

      const { years } = result;

      expect(years).toBe(1);
    });
  });

  describe("formatTimeDifference", () => {
    const testCases = [
      { value: 10, unit: "years", expected: "10 years ago" },
      { value: 1, unit: "years", expected: "1 year ago" },
      { value: 10, unit: "months", expected: "10 months ago" },
      { value: 1, unit: "months", expected: "1 month ago" },
      { value: 3, unit: "weeks", expected: "3 weeks ago" },
      { value: 1, unit: "weeks", expected: "1 week ago" },
      { value: 3, unit: "days", expected: "3 days ago" },
      { value: 1, unit: "days", expected: "1 day ago" },
      { value: 3, unit: "hours", expected: "3 hours ago" },
      { value: 1, unit: "hours", expected: "1 hour ago" },
      { value: 21, unit: "minutes", expected: "21 minutes ago" },
      { value: 2, unit: "minutes", expected: "just now" },
    ];

    testCases.forEach(({ value, unit, expected }) => {
      it(`handles ${value} ${unit} ago`, () => {
        const timeDifference: any = {
          years: 0,
          months: 0,
          weeks: 0,
          days: 0,
          hours: 0,
          minutes: 0,
        };
        timeDifference[unit] = value;
        const text = formatTimeDifference(timeDifference);
        expect(text).toBe(expected);
      });
    });
  });
});
