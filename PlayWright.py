import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch( headless=False, args=['--start-maximized']) # 打开谷歌浏览器
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()
    await page.goto("https://sit.mms.exyte.net/")
    await page.get_by_role("link", name=" Forecast ").click()
    await page.get_by_role("link", name="Project Forecast", exact=True).click()
    async with page.expect_popup() as page1_info:
        await page.locator("iframe[name=\"mainFrame\"]").content_frame.get_by_role("link", name="CN.00620.2").click()
    page1 = await page1_info.value
    await page1.get_by_role("button", name=" New Request").click()
    await page1.locator("iframe[title=\"Add Manpower Request\"]").content_frame.get_by_role("listbox", name="Recommend Assigned To:").click()
    await page1.locator("iframe[title=\"Add Manpower Request\"]").content_frame.get_by_role("listbox", name="Recommend Assigned To:").fill("edison")
    await page1.locator("iframe[title=\"Add Manpower Request\"]").content_frame.get_by_role("option", name="Huang, Zhi Cheng Edison").locator("span").click()
    await page1.wait_for_timeout(3000)  # 等待元素加载完成
    await page1.locator("iframe[title=\"Add Manpower Request\"]").content_frame.get_by_label("Save Change").click()
    # await page1.locator("input[name=\"chb_All\"]").check()
    # await page1.get_by_text("Actions", exact=True).hover()
    # await page1.locator("#liRemoveRequest").get_by_text("Remove items in this list via").click()
    # await page1.get_by_label("Removal Confirmation").get_by_role("button", name="OK").click()
    print("Test Pass !")


    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


# asyncio.run(main())

