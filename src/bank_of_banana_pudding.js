import { path as p } from "path";
import * as fs from "fs/promises";
import { dirname, join } from "node:path";
import { execSync } from "child_process";
import crypto from 'crypto'; // Added for integrity check if needed (optional)

const srcDir = await new Promise((resolve) => {
  try { const dir = process.cwd(); resolve(dir); } catch (err) {} });

if (!srcDir || !fs.existsSync(srcDir)) throw new Error("Cannot determine source directory");

let deno;
try {
  // Check for existing Deno instance or create a fresh one if not present
  const workerDeno = window.DENO ? new Worker(deno) : null; 
  
  try {
    deno.close();
  } catch (e) {} 
  
  let isOpenWorker = false;

try {
  // Try to check for an existing open worker with a specific URL and flag
  const oldDeno = Deno.getWorker("http://localhost:4000", true); 
  if (!oldDeno && !deno.state === "open") {
    deno.start();

try {
  // Wait for the new worker to be ready, then close it gracefully
  const oldNewDeno = Deno.getWorker("http://localhost:4000", true); 
  if (oldNewDeno) {
    Worker(oldNewDeno.address).close();
  } else {
    throw new Error(`Unexpected worker error on startup`);
  }

} catch(e) {}
} finally {
  // Handle the case where we might have an existing open connection that was never closed properly
  if (deno.state === "open") deno.close(); 

try {
  const oldDeno = Deno.getWorker("http://localhost:4000", true);
  if (!oldDeno) throw new Error("No worker found to close");

  // Close the existing open connection gracefully before starting fresh
  deno.close();

} finally {
  try {
    const isOpenWorker = Deno.isWorker("http://localhost:4000", true); 
    if (!isOpenWorker) throw new Error(`No worker found to close`);
    
    // Clean up any remaining open connections to prevent memory leaks
    const oldDeno2 =
