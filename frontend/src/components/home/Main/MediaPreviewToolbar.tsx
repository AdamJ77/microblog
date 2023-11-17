import React from "react";

interface IMediaPreviewToolbar {
  onScale: (scale: number) => void;
  scale: number;
  rotate: number;
  onRotate: (rotate: number) => void;
}

export default function MediaPreviewToolbar({
  onScale,
  scale,
  rotate,
  onRotate,
}: IMediaPreviewToolbar) {
  const toolbarButtons = [
    {
      onclick: () => onScale(scale + 1),
      image: `${process.env.PUBLIC_URL}/icons/zoom_in.svg`,
    },
    {
      onclick: () => onScale(scale - 1),
      image: `${process.env.PUBLIC_URL}/icons/zoom_out.svg`,
    },
    {
      onclick: () => onRotate(rotate + 90),
      image: `${process.env.PUBLIC_URL}/icons/rotate.svg`,
    },
  ];

  return (
    <>
      {toolbarButtons.map((button, index) => (
        <div
          key={index}
          className="PhotoView-Slider__toolbarIcon"
          style={{ width: "42px", height: "42px" }}
          onClick={button.onclick}
        >
          <img src={button.image} />
        </div>
      ))}
    </>
  );
}
