import React from "react";
import { PhotoProvider, PhotoView } from "react-photo-view";
import styles from "./styles/MediaPreview.module.css";
import MediaPreviewToolbar from "./MediaPreviewToolbar";
import { AVAILABLE_VIDEO_EXTENSIONS } from "../../../constants";
import { getMediaStyles } from "./utils/mediaStyles";

interface IMediaPreview {
  media: string[];
}

export default function MediaPreview({ media }: IMediaPreview) {
  const isVideo = (file: string) => {
    const splitted = file.split(".");
    const ext = splitted[splitted.length - 1];
    return AVAILABLE_VIDEO_EXTENSIONS.includes(ext);
  };

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
        {media.map((file, index) => (
          <div
            key={index}
            className={
              media.length % 2 === 1 && index === media.length - 1
                ? styles.single
                : styles.multiple
            }
          >
            {isVideo(file) ? (
              <video
                src={file}
                controls
                loop
                autoPlay
                muted
                style={getMediaStyles(index, media.length)}
                className={styles.file}
              >
                Your browser doesn't support videos
              </video>
            ) : (
              <PhotoView src={file}>
                <img
                  src={file}
                  alt={file}
                  style={getMediaStyles(index, media.length)}
                  className={styles.file}
                  title="preview"
                />
              </PhotoView>
            )}
          </div>
        ))}
      </PhotoProvider>
    </div>
  );
}
