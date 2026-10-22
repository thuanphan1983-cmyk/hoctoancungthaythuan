import React, { useEffect, useRef, useMemo } from 'react';

/**
 * Hiển thị văn bản chứa công thức Toán học bằng KaTeX
 * Nhận diện $...$ (inline) và $$...$$ (display block)
 */
export default function MathView({ text, className = "", block = false }) {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!containerRef.current) return;
    try {
      if (window.renderMathInElement) {
        window.renderMathInElement(containerRef.current, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
            { left: "\\[", right: "\\]", display: true },
            { left: "\\(", right: "\\)", display: false }
          ],
          throwOnError: false
        });
      }
    } catch (e) {
      console.warn("KaTeX render error:", e);
    }
  }, [text]);

  const formatted = useMemo(() => {
    if (!text) return "";
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }, [text]);

  const Tag = block ? "div" : "span";
  return <Tag ref={containerRef} className={className} dangerouslySetInnerHTML={{ __html: formatted }} />;
}
