import { CSSProperties } from "react";

const borderRadius = "10px";

export const getMediaStyles = (index: number, all: number): CSSProperties => {
  if (all === 1 && index === 0) return { borderRadius };
  if (all === 2) {
    return index === 0
      ? {
          borderTopLeftRadius: borderRadius,
          borderBottomLeftRadius: borderRadius,
        }
      : {
          borderBottomRightRadius: borderRadius,
          borderTopRightRadius: borderRadius,
        };
  }
  // more than 2 files
  if (index === 0) return { borderTopLeftRadius: borderRadius };
  if (index === 1) return { borderTopRightRadius: borderRadius };
  if (all % 2 === 1 && index === all - 1)
    return {
      borderBottomLeftRadius: borderRadius,
      borderBottomRightRadius: borderRadius,
    };
  if (index === all - 2) return { borderBottomLeftRadius: borderRadius };
  if (index === all - 1) return { borderBottomRightRadius: borderRadius };
  return {};
};
