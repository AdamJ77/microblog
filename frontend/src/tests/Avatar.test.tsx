import React from "react";
import Avatar from "../components/home/Avatar";
import { render } from "@testing-library/react";

describe("Avatar component", () => {
  // test example

  it("should render correctly", () => {
    const image = "http://some/url";
    const alt = "Couldn't display image";

    const { getByAltText } = render(<Avatar image={image} alt={alt} />);

    expect(getByAltText(alt)).toBeInTheDocument();
  });
});
