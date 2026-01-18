from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # visible for debugging
    context = browser.new_context()
    page = context.new_page()

    # Step 1: Load site
    page.goto("http://51.195.24.179:8000/")
    page.wait_for_timeout(3000)

    # Step 2: Confirm cookies
    print("[+] Cookies:")
    for c in context.cookies():
        print(c)

    # Step 3: Wait for inputs
    page.wait_for_selector("input", timeout=10000)

    # Step 4: Fill form (CORRECT WAY)
    page.get_by_placeholder("Username").fill("ctf_user_123")
    page.get_by_placeholder("Email").fill("ctf_user_123@gmail.com")
    page.get_by_placeholder("Password").fill("Password@123")

    # Step 5: Submit
    page.get_by_role("button", name="Register").click()

    # Step 6: Wait & print result
    page.wait_for_timeout(3000)
    print("\n[+] Page Output:")
    print(page.inner_text("body"))

    browser.close()
