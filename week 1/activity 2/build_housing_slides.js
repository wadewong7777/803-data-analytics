const pptxgen = require("pptxgenjs");
const { imageSizingContain } = require("./pptxgenjs_helpers/image");
const {
  warnIfSlideHasOverlaps,
  warnIfSlideElementsOutOfBounds,
} = require("./pptxgenjs_helpers/layout");

const pptx = new pptxgen();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "Yoobee Data Analytics";
pptx.subject = "Initial story from Housing Prices Dataset";
pptx.title = "Housing Prices Dataset: Initial Story";
pptx.company = "Yoobee";
pptx.lang = "en-US";
pptx.theme = {
  headFontFace: "Arial",
  bodyFontFace: "Arial",
  lang: "en-US",
};
pptx.defineLayout({ name: "CUSTOM_WIDE", width: 13.333, height: 7.5 });
pptx.layout = "CUSTOM_WIDE";
pptx.margin = 0;
pptx.slideWidth = 13.333;
pptx.slideHeight = 7.5;
pptx.notesSlide = true;
pptx.layout = "LAYOUT_WIDE";

const W = 13.333;
const H = 7.5;
const C = {
  bg: "F7FAFC",
  ink: "1F2933",
  muted: "52606D",
  blue: "4C78A8",
  teal: "72B7B2",
  green: "54A24B",
  amber: "F58518",
  red: "E45756",
  line: "D9E2EC",
  white: "FFFFFF",
};

const notes = [
  "This dataset contains 545 houses and 13 columns. The main question is simple: why are some houses much more expensive than others? The median price is 4.34 million, while the average is 4.77 million. Because the average is higher than the median, the dataset has some expensive houses pulling the average upward.",
  "Most houses are grouped around the middle price range. The histogram shows many homes between about 3 million and 6 million. A smaller number of high-priced houses sit above that range, reaching up to 13.30 million. This tells us the story is not only about the average price. We also need to understand what separates the high-end homes.",
  "The clearest numeric relationship is area. When the houses are split into four area groups, the average price rises from 3.54 million in the smallest group to 6.22 million in the largest group. This suggests that bigger homes are usually valued higher, and area should be one of the first variables to consider in any deeper analysis.",
  "Size is not the only part of the story. Houses with air conditioning, main road access, a preferred area, or a guest room have higher average prices than houses without those features. Air conditioning has the biggest simple difference, about 1.82 million. Main road access and preferred area are also strong. These are descriptive differences, so they show patterns, not guaranteed causes.",
  "The initial story is that housing price is shaped by three ideas: space, comfort, and location access. Larger houses tend to cost more. Comfort features make a house more attractive. Location features such as main road access and preferred area also lift the average price. The next step would be to build a regression model to test these drivers together and check which features still matter when the others are included.",
];

function text(slide, value, x, y, w, h, opts = {}) {
  slide.addText(value, {
    x, y, w, h,
    fontFace: "Arial",
    color: opts.color || C.ink,
    fontSize: opts.fontSize || 18,
    bold: opts.bold || false,
    margin: opts.margin || 0,
    breakLine: opts.breakLine || false,
    fit: "shrink",
    valign: opts.valign || "top",
    align: opts.align || "left",
    paraSpaceAfterPt: opts.paraSpaceAfterPt || 0,
    ...opts,
  });
}

function addHeader(slide, title, index) {
  slide.background = { color: C.bg };
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: W, h: 0.12, fill: { color: C.blue }, line: { color: C.blue } });
  text(slide, title, 0.55, 0.38, 9.7, 0.55, { fontSize: 24, bold: true });
  text(slide, `Housing Prices Dataset | ${index}/5`, 10.3, 0.44, 2.45, 0.35, { fontSize: 10.5, color: C.muted, align: "right" });
  slide.addShape(pptx.ShapeType.line, { x: 0.55, y: 1.05, w: 12.2, h: 0, line: { color: C.line, width: 1 } });
}

function addMetric(slide, label, value, x, y, color) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y, w: 2.75, h: 1.05,
    rectRadius: 0.08,
    fill: { color: C.white },
    line: { color: C.line, width: 1 },
  });
  text(slide, value, x + 0.18, y + 0.18, 2.39, 0.32, { fontSize: 22, bold: true, color });
  text(slide, label, x + 0.18, y + 0.62, 2.39, 0.22, { fontSize: 10.5, color: C.muted });
}

function addBullets(slide, items, x, y, w, h) {
  slide.addText(items.map(item => ({ text: item, options: { bullet: { type: "ul" } } })), {
    x, y, w, h,
    fontFace: "Arial",
    fontSize: 17,
    color: C.ink,
    breakLine: false,
    fit: "shrink",
    paraSpaceAfterPt: 11,
    margin: 0,
  });
}

function addImage(slide, path, x, y, w, h) {
  slide.addImage({ path, ...imageSizingContain(path, x, y, w, h) });
}

function addNotesAndCheck(slide, note, index) {
  slide.addNotes(note);
  warnIfSlideHasOverlaps(slide, pptx, { ignoreDecorativeShapes: true, ignoreLines: true });
  warnIfSlideElementsOutOfBounds(slide, pptx);
}

let slide = pptx.addSlide();
slide.background = { color: C.bg };
slide.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: W, h: H, fill: { color: C.bg }, line: { color: C.bg } });
slide.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: 0.18, h: H, fill: { color: C.blue }, line: { color: C.blue } });
text(slide, "Housing Prices Dataset", 0.75, 0.72, 8.4, 0.55, { fontSize: 27, bold: true });
text(slide, "An initial 3-minute story about what seems to drive house prices", 0.75, 1.35, 9.7, 0.42, { fontSize: 16.5, color: C.muted });
text(slide, "The question", 0.75, 2.17, 2.0, 0.35, { fontSize: 14, bold: true, color: C.blue });
text(slide, "Why are some houses much more expensive than others?", 0.75, 2.58, 6.4, 0.85, { fontSize: 26, bold: true, color: C.ink });
addMetric(slide, "houses in the dataset", "545", 0.75, 4.15, C.blue);
addMetric(slide, "columns", "13", 3.78, 4.15, C.teal);
addMetric(slide, "median price", "4.34M", 6.81, 4.15, C.green);
addMetric(slide, "highest price", "13.30M", 9.84, 4.15, C.red);
text(slide, "Initial story: price appears to rise with space, comfort features, and location access.", 0.75, 6.12, 10.6, 0.35, { fontSize: 17, color: C.ink });
addNotesAndCheck(slide, notes[0], 1);

slide = pptx.addSlide();
addHeader(slide, "1. The market has a strong middle", 2);
addImage(slide, "housing_price_distribution.png", 0.55, 1.35, 7.55, 5.45);
text(slide, "What the distribution says", 8.45, 1.45, 3.8, 0.35, { fontSize: 19, bold: true, color: C.blue });
addBullets(slide, [
  "Most houses sit between about 3M and 6M.",
  "The average price is higher than the median.",
  "A smaller high-end group pulls the average upward.",
], 8.45, 2.05, 4.15, 2.6);
text(slide, "Story point: start with the middle market, then explain what pushes some homes above it.", 8.45, 5.3, 3.9, 0.8, { fontSize: 15, color: C.ink });
addNotesAndCheck(slide, notes[1], 2);

slide = pptx.addSlide();
addHeader(slide, "2. Size is the clearest price driver", 3);
addImage(slide, "housing_area_quartiles.png", 0.55, 1.35, 7.55, 5.45);
text(slide, "Main evidence", 8.45, 1.45, 3.8, 0.35, { fontSize: 19, bold: true, color: C.green });
addBullets(slide, [
  "Area has the strongest numeric relationship with price.",
  "Average price rises from 3.54M to 6.22M across area groups.",
  "Bigger homes are the easiest first explanation for higher prices.",
], 8.45, 2.05, 4.15, 3.0);
text(slide, "Correlation with price: area 0.54, bathrooms 0.52, stories 0.42.", 8.45, 5.65, 3.9, 0.5, { fontSize: 13.5, color: C.muted });
addNotesAndCheck(slide, notes[2], 3);

slide = pptx.addSlide();
addHeader(slide, "3. Comfort and access add premiums", 4);
addImage(slide, "housing_feature_premiums.png", 0.55, 1.35, 7.75, 5.45);
text(slide, "Feature pattern", 8.6, 1.45, 3.65, 0.35, { fontSize: 19, bold: true, color: C.amber });
addBullets(slide, [
  "Air conditioning has the largest simple premium: about 1.82M.",
  "Main road access and preferred area also show strong premiums.",
  "These are descriptive patterns, not proof of causation.",
], 8.6, 2.05, 3.95, 3.0);
text(slide, "Story point: buyers appear to pay more for practical comfort and easier access.", 8.6, 5.63, 3.75, 0.65, { fontSize: 14.5, color: C.ink });
addNotesAndCheck(slide, notes[3], 4);

slide = pptx.addSlide();
addHeader(slide, "4. Initial story for discussion", 5);
text(slide, "Housing price looks like a mix of three ideas:", 0.75, 1.45, 7.4, 0.45, { fontSize: 23, bold: true });
const takeaways = [
  { title: "Space", body: "Larger area is linked with higher average price.", color: C.blue },
  { title: "Comfort", body: "Air conditioning and guest rooms lift the average price.", color: C.green },
  { title: "Access", body: "Main road and preferred area homes sell at higher averages.", color: C.amber },
];
takeaways.forEach((item, i) => {
  const x = 0.8 + i * 4.15;
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y: 2.35, w: 3.65, h: 2.25,
    rectRadius: 0.08,
    fill: { color: C.white },
    line: { color: C.line, width: 1 },
  });
  slide.addShape(pptx.ShapeType.rect, { x, y: 2.35, w: 3.65, h: 0.12, fill: { color: item.color }, line: { color: item.color } });
  text(slide, item.title, x + 0.22, 2.72, 3.2, 0.32, { fontSize: 21, bold: true, color: item.color });
  text(slide, item.body, x + 0.22, 3.25, 3.15, 0.82, { fontSize: 15.5, color: C.ink });
});
text(slide, "Next step", 0.75, 5.35, 1.4, 0.3, { fontSize: 15, bold: true, color: C.blue });
text(slide, "Build a regression model to test these drivers together and separate real signal from overlapping effects.", 0.75, 5.8, 10.9, 0.55, { fontSize: 19, bold: true, color: C.ink });
text(slide, "Use this deck as an initial story, not a final model.", 0.75, 6.6, 8.0, 0.3, { fontSize: 13.5, color: C.muted });
addNotesAndCheck(slide, notes[4], 5);

pptx.writeFile({ fileName: "housing_prices_story.pptx" })
  .then(() => console.log("Saved housing_prices_story.pptx"))
  .catch((err) => {
    console.error(err);
    process.exit(1);
  });
