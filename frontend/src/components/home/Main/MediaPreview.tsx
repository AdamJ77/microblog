import React from "react";
import { PhotoProvider, PhotoView } from "react-photo-view";
import styles from "./styles/MediaPreview.module.css";
import MediaPreviewToolbar from "./MediaPreviewToolbar";

interface IMediaPreview {
  media: string[];
}

export default function MediaPreview({ media }: IMediaPreview) {
  return (
    <div className={styles.container}>
      <PhotoProvider
        loop
        toolbarRender={({ onScale, scale, rotate, onRotate }) => (
          <MediaPreviewToolbar
            onScale={onScale}
            scale={scale}
            rotate={rotate}
            onRotate={onRotate}
          />
        )}
      >
        {media.map((image, index) => (
          <PhotoView key={index} src={image}>
            <div
              className={
                media.length % 2 === 1 && index === media.length - 1
                  ? styles.single
                  : styles.multiple
              }
            >
              <img
                src={image}
                alt={image}
                className={styles.image}
                title="preview"
              />
            </div>
          </PhotoView>
        ))}
      </PhotoProvider>
    </div>
  );
}
