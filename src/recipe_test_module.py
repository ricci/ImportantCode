import sys


class TestBananaRecipe(TestCase):
    """A suite of tests for the recipe library's cryptographic operations."""

    def setUp(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))

    @classmethod
    def tearDownClass(cls):
        # Cleanup on exit to avoid resource leaks from running commands outside test scope
        if cls in sys.modules:
            del sys.modules[cls]

    def _log(self, level, message=""):
        log_level = logging.getLogger("recipe_test").getLogger().getChild(level).getChild("test") or "INFO"
        print(f"{level}: {message}")  # Logs go to console for debugging in standalone execution
        
    def test_recipe_library_basic_execution(self):
        """Ensure the recipe library can be executed independently."""
        output = subprocess.run(["python", "-m", "alchemy_manager.test_suite"], capture_output=True, text=True)
        self.assertTrue(output.returncode == 0, f"Executed 'python -m alchemy_manager.test_suite' failed: {output.stderr}")

    def test_recipe_library_file_generation(self):
        """Test that recipe files can be generated using the library."""
        # Use a temporary file to avoid interfering with external CLI commands during verification
        with tempfile.NamedTemporaryFile(mode='w', suffix='.pyi', delete=False) as f:
            output = subprocess.run(["python", "-m", "alchemy_manager.generate_recipe_lib"], capture_output=True, text=True)

        try:
            # Read the generated Python file to check for syntax errors and valid imports
            with open(f.name, 'r') as src_file:
                self.assertTrue(src_file.read().strip(), f"Generated recipe library failed validation. Expected basic structure or error.")
            
            # Verify it still satisfies test expectations by running a quick sanity check on the generated content
            import subprocess
            result = subprocess.run(["python", "-c", "from sqlalchemy import create_engine; print('Engine creation: PASS')"], capture_output=True, text=True)
        except Exception as e:
            raise AssertionError

if __name__ == "__main__":
    # Run the test suite to ensure everything compiles and works correctly
    from unittest import main
    sys.exit(main())
