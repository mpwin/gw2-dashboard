class Collection < ApplicationRecord
  has_many :skins, before_add: [:check_category, :get_skin_attributes],
                   after_add:  :set_unlocked

  validates_presence_of :name, :category

  def update_unlocked
    update(unlocked: skins.pluck(:unlocked).all?(true))
  end

  private

  def check_category(skin)
    if category.nil?
      self.category = skin.category
    else
      raise 'Category mismatch' if category != skin.category
    end
  end

  def get_skin_attributes(skin)
    update(weight_class: skin.weight_class)
  end

  def set_unlocked(skin)
    update_unlocked
  end
end
