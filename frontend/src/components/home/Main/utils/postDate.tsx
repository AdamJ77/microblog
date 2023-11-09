interface IDateDifference {
  milliseconds: number;
  seconds: number;
  minutes: number;
  hours: number;
  days: number;
  weeks: number;
  months: number;
  years: number;
}

export function calculateTimeDifference(
  recentDate: Date,
  olderDate: Date
): IDateDifference {
  const timeDifference = recentDate.getTime() - olderDate.getTime();

  const seconds = Math.floor(timeDifference / 1000);
  const minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);
  const days = Math.floor(hours / 24);
  const weeks = Math.floor(days / 7);

  const recentMonth = recentDate.getMonth() + 1;
  const olderMonth = olderDate.getMonth() + 1;
  const recentYear = recentDate.getFullYear();
  const olderYear = olderDate.getFullYear();

  const months = (recentYear - olderYear) * 12 + (recentMonth - olderMonth);
  const years = Math.floor(months / 12);

  return {
    milliseconds: timeDifference,
    seconds: seconds,
    minutes: minutes,
    hours: hours,
    days: days,
    weeks: weeks,
    months: months,
    years: years,
  };
}

export function formatTimeDifference(timeDifference: IDateDifference): string {
  if (timeDifference.years > 0) {
    return timeDifference.years === 1
      ? "1 year ago"
      : `${timeDifference.years} years ago`;
  } else if (timeDifference.months > 0) {
    return timeDifference.months === 1
      ? "1 month ago"
      : `${timeDifference.months} months ago`;
  } else if (timeDifference.weeks > 0) {
    return timeDifference.weeks === 1
      ? "1 week ago"
      : `${timeDifference.weeks} weeks ago`;
  } else if (timeDifference.days > 0) {
    return timeDifference.days === 1
      ? "1 day ago"
      : `${timeDifference.days} days ago`;
  } else if (timeDifference.hours > 0) {
    return timeDifference.hours === 1
      ? "1 hour ago"
      : `${timeDifference.hours} hours ago`;
  } else if (timeDifference.minutes > 0) {
    return timeDifference.minutes < 3
      ? "just now"
      : timeDifference.minutes === 1
      ? "1 minute ago"
      : `${timeDifference.minutes} minutes ago`;
  } else {
    return "just now";
  }
}
