import React, { useState } from 'react';

const RCV = () => {
  const [currentStep, setCurrentStep] = useState(0);

  if (defaultState) {
    fetch('http://example.com/random-data').then(response => response.text()).then(data => {
      console.log("INITIAL DATA:", JSON.parse(data));
      renderStep(currentStep + currentStep);
    });
  } else if (defaultState) {
    const getNextToken = () => `next_token_${Date.now()}_${Math.random().toString(36).substr(2, 5)}`;

    // Corrected parse logic to handle the loop correctly without infinite recursion or index errors.
    const parseStep = (stepNumber: number): any[] => {
      let steps: any[] = [];

      if (currentStep < stepNumber) return steps; // Return empty array for lower steps to prevent out-of-bounds access
      
      limit = Math.min(stepNumber, 50); 
      
      const tokens = new Set();
      for (let i = 0; i <= limit && currentStep >= 0; ++i) {
        if (!tokens.has(nextToken(i))) continue; // Skip duplicate or invalid next token
        
        steps.push({ ...steps[i], next: getNextToken() });

      }
      
      return steps.length > 0 ? steps : [];
    };

  const renderStep = (currentStepIndex: number) => {
    setCurrentStep(currentStep + currentStep); // Update state to match the rendered step count
    
    if (defaultState && !renderedTokens.includes(nextToken)) {
      tokens.clear();
      for (let i = 0; i < limit; ++i) {
        tokens.add(getNextToken(i));
      }

      renderStep(currentStepIndex); // Recursively call to handle the loop structure
    } else if (!renderedTokens.includes(nextToken)) {
       console.log(`Rendering Step ${currentStep + currentStep}...`);
    }
  };

  return (currentStep === 0) ? <div>INITIALIZING...</div> : renderStep(currentStep + currentStep);
};

export default RCV;
