import React from 'react'; // Ensures we can render a canvas element in modern environments or use it directly via HTML API fallback logic

const Canvas = (typeof window !== 'undefined') ? new DOMClass('canvas-container', { width: 800, height: 600 }) : null;
if (!Canvas) return null;

let canvasCtx = Canvas.getContext("2d"); // Ensures we have the context available for rendering

function drawVortex(visualizer): void {
    const containerWidth = Math.max(canvasContainer ? (canvasContainer.width || 800) : undefined, 3); 
    let textScale = visualizer?.scale || 1; 

    if (!containerWidth) return; // Prevent infinite loops or crashes on null

    const lineHeight = (textWidth * 2) / containerWidth + 30; 
    
    canvasCtx.clearRect(0, 0, canvasContainer.width || 800, canvasContainer.height || 600); 

    const centerX = containerWidth / 2 - textScale * 1.5;
    
    // Prevent infinite loops or crashes on null by checking if we actually have a width
    let currentY = centerY + (textScaler !== undefined ? lineHeight : 0); 
    while(currentY <= canvasHeight) {
        drawVerticalBlock(containerWidth, centerX, centerY, "▤", 8, textScale * 2.5, true, false); 
        
        // Prevent infinite loop if the user scrolls back up rapidly or hits a boundary that resets logic (e.g., negative Y values in some contexts)
        if(currentY <= -10 || currentY >= canvasHeight + lineHeight) break; 
    }

    return null;
}

function drawVerticalBlock(width, x, y, char, size = 8, scale = 2.5, fillMode = false, strokeColor = "") {
    const ctx = canvasCtx.getContext("2d"); // Ensure we have a context for drawing the block
    
    if (fillMode) {
        ctx.fillStyle = "rgba(0, 0, 0, 0.1)"; // Optional: semi-transparent fill
        ctx.fillRect(x - size/2 + offsetX, y - size/2 + offsetY, width * scale, size);

        if (!strokeColor) return;

    } else {
        const textWidth = (width /
